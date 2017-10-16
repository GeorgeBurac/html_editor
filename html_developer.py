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


def property_address_editor(Beautiful_Soup_object, new_address):
    current_address = Beautiful_Soup_object.find("div", {"class":"property_unit_custom_element property_address unit_element_43931 "}).text
    

    
def update_title(Beautiful_Soup_object, new_title):
    title = Beautiful_Soup_object.h4.text
    title_html = str(Beautiful_Soup_object.h4).replace(title, new_title)
    html_string =  str(Beautiful_Soup_object).replace(title, title_html)
    return html_string

def update_price(Beautiful_Soup_object, new_price):
    """This function updates the price detail of the BeautifulSoup object provided, 
    using the new price parameter."""
    price_html = Beautiful_Soup_object.find("span", {"class":"price_label price_label_before"}).next_sibling
    price = str(price_html).strip()

def short_description_editor(Beautiful_Soup_object, desired_description):
    """This function edits the short description of the ad. It replaces the old 
    short description of the ad with the desired description. The function takes 
    a BeautifulSoup object as a parameter and the desired description."""
    div = Beautiful_Soup_object.find("div", {"class":"property_unit_custom_element description unit_element_15489 "})
    old_description = div.text
    new_div = str(div).replace(old_description, desired_description)
    return new_div  


def html_developer(source_file, html_file):
    f = open(source_file, "r").read()
    html_file = open(html_file, "r").read()
    Beautiful_Soup_object = BeautifulSoup(html_file, "html.parser")
    
    for line in range(1, len(f)):
        line = line.strip().split(",")
        property_title, price, beds, bathrooms, description, property_overview, agent, short_ad_description = line
        div_short_description = short_description_editor(Beautiful_Soup_object, short_ad_description)
         
        

def main():
    source_file = sys.stdin.readline().strip()
    html_developer(source_file)


if __name__ == "__main__":
    main()
