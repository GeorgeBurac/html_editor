import sys
from bs4 import BeautifulSoup
import os


def ad_link_editor(Beautiful_Soup_object, new_link):
    """This function will replace the link of the ad and return a
    new html file containing the desired ad.
    The function takes as parameters a BeautifulSoup object and the new link desired."""
    div = Beautiful_Soup_object.find("div", {"class":"item active"})# selects the div
    old_ad_link = div.find("a")["href"] # selects the link to be replaced
    edited_div = str(div).replace(old_ad_link, new_link)
    new_div = str(Beautiful_Soup_object).replace(edited_div, new_div)
    return new_div.prettify()




def image_link_editor(Beautiful_Soup_object, desired_image_link):
    """This function edits the BeautifulSoup object provided as a parameter,
    replacing the links in the src and data-original tags
    with the desired link provided."""
    div = Beautiful_Soup_object.find("div", {"class":"listing-unit-img-wrapper"})# selects the div
    old_image_src_links = div.findAll("a")["src"]
    old_image_data_original_links = div.findAll("a")["data-original"]
    for old in zip(old_image_src_links, old_image_data_original_link):
        edited_div = str(div).replace(old_image_src_link, desired_image_link)
        edited_div = edited_div.replace(old_image_data_original_link, desired_image_link)
    return edited_div.prettify()


def alt_tag_editor(Beautiful_Soup_object, desired_image_description):
    """This function edits the alt tag. It changes the alt description to the
    desired image description. The function uses a BeautifulSoup object as a
    parameter and the desired image description."""
    div = Beautiful_Soup_object.find("div", {"class":"item active"})# selects the div
    old_alt_tag = div.find("a")["alt"]
    alt_tag = old_alt_tag.replace("", desired_image_description)
    tag = "alt=" + old_alt_tag
    new_div = str(div).replace(tag, "alt=" + desired_image_description)
    return new_div


def property_address_editor(string, new_address):
    """This function updates the address of the property with the new address provided."""
    Beautiful_Soup_object = BeautifulSoup(string, "html.parser")
    class_name = "property_unit_custom_element property_address unit_element_43931 "
    current_address = Beautiful_Soup_object.find("div", {"class":class_name}).text
    string = string.replace(current_address, new_address)
    return BeautifulSoup(string, "html.parser").prettify()



def update_title(string, new_title):
    """This function updates the title of the property, by replacing the old title
    with the new title provided."""
    Beautiful_Soup_object = BeautifulSoup(string, "html.parser")
    old_title = Beautiful_Soup_object.h4.text
    html_string =  str(Beautiful_Soup_object).replace(old_title, new_title)
    return BeautifulSoup(html_string, "html.parser").prettify()

def update_price(string, new_price):
    """This function updates the price detail of the string provided,
    using the new price parameter."""
    Beautiful_Soup_object = BeautifulSoup(string, "html.parser")
    price_html = Beautiful_Soup_object.find("span", {"class":"price_label price_label_before"}).next_sibling
    old_price = str(price_html).strip()
    string = string.replace(old_price, new_price)
    return BeautifulSoup(string, "html.parser").prettify()


def short_description_editor(string, desired_description):
    """This function edits the short description of the ad. It replaces the old
    short description of the ad with the desired description. The function takes
    a BeautifulSoup object as a parameter and the desired description."""
    Beautiful_Soup_object = BeautifulSoup(string, "html.parser")
    div = Beautiful_Soup_object.find("div", {"class":"property_unit_custom_element description unit_element_15489 "})
    old_description = div.text
    edited_description = str(div).replace(old_description, desired_description)
    return BeautifulSoup(new_div, "html.parser").prettify()


def html_developer(data_source_file, template_html_file):
    # open and read the source file for the data to be written
    data_source_file = open(data_source_file, "r")
    data_to_write = data_source_file.read().split("\n")
    # open and read the html template
    template_html_file = open(template_html_file, "r")
    template_data = template_html_file.read()
    template_html_file.close()
    Beautiful_Soup_object = BeautifulSoup(template_data, "html.parser")
    for n in range(1, len(data_to_write)):

        line = data_to_write[n].strip().split(",")

        property_title =  line[0]
        price = line[1]
        beds = line[2]
        bathrooms = line[3]
        description = line[4]
        property_overview = line[5]
        agent = line[6]
        short_ad_description = line[7:]


        title_update = update_title(Beautiful_Soup_object, property_title) # it's html
        short_description_update = short_description_editor(title_update, short_ad_description)
        price_update = update_price(short_description_update)

        template_html_file = open(property_title + ".csv", "w")

        template_html_file.write(price_update)

def main():
    data_source_file = r"C:\Users\George Burac\Desktop\p2\NSD\AlinProjects\Daft Scraper\scraped data.csv"

    template_html_file = r"C:\Users\George Burac\Desktop\p2\NSD\AlinProjects\Daft Scraper\property_eire.html"
    html_developer(data_source_file, template_html_file)


if __name__ == "__main__":
    main()
