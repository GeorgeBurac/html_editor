import sys
from bs4 import BeautifulSoup
import os


def ad_link_editor(Beautiful_Soup_object, new_link):
    """This function will replace the link of the ad and return a new html file containing the desired ad.
    The function takes as parameters a BeautifulSoup object and the new link desired."""
    div = Beautiful_Soup_object.find("div", {"class":"item active"})# selects the div
    old_ad_link = div.find("a")["href"] # selects the link to be replaced
    edited_div = str(div).replace(old_ad_link, new_link)
    new_div = str(Beautiful_Soup_object).replace(edited_div, new_div)
    return new_div.prettify()


def image_link_editor(Beautiful_Soup_object, desired_image_link):
    """This function edits the BeautifulSoup object provided as a parameter, replacing the links in the src and data-original tags
    with the desired link provided."""
    div = Beautiful_Soup_object.find("div", {"class":"listing-unit-img-wrapper"})# selects the div
    old_image_src_links = div.findAll("a")["src"]
    old_image_data_original_links = div.findAll("a")["data-original"]
    for old in zip(old_image_src_links, old_image_data_original_link):
        edited_div = str(div).replace(old_image_src_link, desired_image_link)
        edited_div = edited_div.replace(old_image_data_original_link, desired_image_link)
    return edited_div.prettify()


def alt_tag_editor(Beautiful_Soup_object, desired_image_description):
    div = Beautiful_Soup_object.find("div", {"class":"item active"})# selects the div
    old_alt_tag = div.find("a")["alt"]
    alt_tag = old_alt_tag.replace("", desired_image_description)
    tag = "alt=" + old_alt_tag
    new_div = str(div).replace(tag, "alt=" + desired_image_description)
    return new_div.prettify()


def description_editor(Beautiful_Soup_object, desired_description):
    div = Beautiful_Soup_object.find("div", {"class":"property_unit_custom_element description unit_element_15489 "})
    return div.text
def html_developer(source_file, destination_file=None):
    f = open(source_file, "r").read()

    for line in range(1, len(f)):
        line = line.strip().split(",")
        property_title_with_address_and_type, house_price, number_of_beds, number_of_bathrooms, description, property_overview, agent = line

    i = 0

def main():
    source_file = sys.stdin.readline().strip()
    html_developer(source_file)


if __name__ == "__main__":
    main()
