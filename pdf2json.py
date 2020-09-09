import sys
import io
import re
import json
import argparse

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams
from pdfminer.converter import PDFConverter


password = b""
pagenos = set()
maxpages = 0
caching = True
outtype = "text"


def _get_content(fname):
    rsrcmgr = PDFResourceManager(caching=caching)
    laparams = LAParams()
    laparams.line_margin = 1.0
    laparams.boxes_flow = 1.0
    imagewriter = None
    with io.BytesIO() as outfp:
        device = TextConverter(
            rsrcmgr, outfp, laparams=laparams, imagewriter=imagewriter
        )
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        with open(fname, "rb") as f:
            for page in PDFPage.get_pages(
                f,
                pagenos,
                maxpages=maxpages,
                password=password,
                caching=caching,
                check_extractable=True,
            ):
                interpreter.process_page(page)
        return outfp.getvalue().decode("utf-8")


def _parse(content):
    """Parse the content of the Resume pdf and return the sections with detail"""
    # add NULL to prefix and suffix of the heading
    # to easily split the sections
    sections = (
        section.strip()
        for section in re.sub(r"(\w+.*\w+)\s+_{2,}", "\0\g<1>\0", content).split("\x00")
        if section.strip()
    )

    # iter_sections = iter(sections)
    detail = next(sections)  # this one will be the head contain name, phone and address

    # x = [(a,b) for a,b in zip(sections[1::2], sections[2::2])]
    x = [(heading, body) for heading, body in zip(sections, sections)]

    match = re.search(
        r"(?P<name>\w+\s*\w+)\s*(?P<phone>\(\w+\)\s*(\w+)\-(\w+))\W+(?P<email>.*@.[^ ]*)\W+(?P<address>.*)",
        detail,
    )
    if match:
        details = match.groupdict()

    details = {k.strip(): v.strip() for k, v in details.items()}

    for k, v in x:
        details[k] = "".join(line.strip() for line in v.strip().split("\n"))

    return details


def pdf2json(pdf_fname, json_file):
    """Dump details in JSON from resume pdf"""
    content = _get_content(pdf_fname)
    data = _parse(content)
    json.dump(data, json_file, indent=4, ensure_ascii=False)


def main():
    parser = argparse.ArgumentParser(description="Convert Resume PDF to JSON")
    parser.add_argument(
        "-i",
        "--infile",
        required=True,
        help="input file name of the PDF for the converter",
    )
    parser.add_argument(
        "-o",
        "--outfile",
        type=argparse.FileType("w"),
        default=sys.stdout,
        help="output file name to save JSON",
    )

    args = parser.parse_args()
    sys.exit(pdf2json(args.infile, args.outfile))


if __name__ == "__main__":
    main()

import unittest
import os


class PDF_TO_JSON_TestCase(unittest.TestCase):
    def setUp(self):
        self.fname = os.path.join(sys.prefix, "test_data/Interview_sample_data.pdf")

    def test_content_not_empty(self):
        content = _get_content(self.fname)
        self.assertTrue(len(content) > 0)

    def test_headers_exist(self):
        headers = {
            "name",
            "phone",
            "email",
            "address",
            "Education",
            "Leadership Experience",
            "Professional Experience",
            "Additional Projects",
            "Skills & Interests",
        }
        content = _get_content(self.fname)
        data = _parse(content)
        self.assertEqual(data.keys(), headers)
