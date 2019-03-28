# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: te_requests_post.py
@time: 2019/3/27
"""

import requests
import zlib
import time


json_data = '{"meta": {"build":   "3.18.7", "_links": {"self": {"href": "https://mapi-ng.rdc.moveaws.com/api/v1/properties/1000381744?client_id=rdc_mobile_native%2C9.3.7%2Candroid"}}, "schema": "core.2", "tracking": "type|meta|data|resource_type|property_detail|query|client_id|rdc_mobile_native,9.3.7,android|schema|core.2^^^$0|1|2|$3|4|5|$6|7|8|9]]]", "matching_rows": 1, "returned_rows": 1, "tracking_params": {"zip": "93446", "city": "Paso Robles", "mprId": "1000381744", "state": "CA", "subId": "unknown", "planId": "unknown", "version": "1.0", "pageType": "ldp", "listingId": "616843964", "listingMls": "MRCA", "photoCount": "2", "communityId": "unknown", "listingBeds": "", "listingSqFt": "unknown", "productType": "core.agent,basic_opt_in", "leadDelivery": "co_broke", "listingBaths": "0", "listingPrice": "74500", "neighborhood": "unknown", "propertyType": "ldp:land", "propertyStatus": "for_sale", "listingActivity": "active", "leadEnhancements": "classic", "rentalDataSource": "unknown", "advertiserIdAgent": "597675", "ldpPropertyStatus": "ldp:for_sale", "advertiserIdOffice": "2906294", "listingEnhancements": "broker-phone-btm"}}, "properties": [{"mls": {"id": "NS18223217", "name": "CRMLS", "disclaimer": {"href": null, "text": "© 2019, California Regional Multiple Listing Service, Inc.  All Rights Reserved.", "photo": null}, "abbreviation": "MRCA"}, "raw": {"status": "Active", "tax_amount": null}, "beds": null, "baths": 0, "price": 74500, "trend": {"geo": {"city": "Paso Robles", "state_code": "CA"}, "year": 2018, "month": 12, "median": {"age_days": 52, "closing_price": 487500, "listing_price": 499000, "listing_price_sqft": 283, "rental_listing_price": null}, "listing_count": {"sold": 101, "rental": 6, "for_sale": 379}, "hotmarket_rank": null, "hotmarket_index": null, "active_listing_count": 379, "hotmarket_temperature": null, "sales_to_inventory_count_percent": 26.65, "asking_to_sold_price_percent_change": -1.91, "sales_to_inventory_count_percent_market_type": "Seller"}, "_links": {"self": {"href": "https://mapi-ng.rdc.moveaws.com/api/v1/properties/M1000381744?client_id=rdc_mobile_native%2C9.3.7%2Candroid&schema=core.2&listing_id=616843964"}}, "agents": [{"id": "597675", "href": "", "name": "Cristina Sirotta", "email": "cristinasirotta@gmail.com", "photo": {"href": "https://p.rdcpix.com/v01/ac28b355e-m0l.jpg"}, "slogan": "", "nrds_id": "207099237", "primary": true, "office_name": "Re/Max Parkside Real Estate", "profile_name": "Cristina Sirotta", "advertiser_id": "597675", "mls_memberships": {"member": {"id": "ATSIROTTAC", "name": "Cristina Sirotta", "abbreviation": "MRCA", "agent_system_id": "ATSIROTTAC", "office_system_id": "PRREMAX"}}, "nrds_verified_id": "207099237", "nrds_verification_method": "Claimed"}], "broker": {"name": "Re/Max Parkside Real Estate", "phone1": {"type": "broker", "number": "(805) 239-3310"}}, "office": {"id": "7f76e99736a27fc80e59d109c92b450b", "href": "WWW.PARKSIDEREALTORS.COM", "name": "Re/Max Parkside Real Estate", "email": "ekwilliams@remax.net", "photo": {"href": ""}, "phones": [{"type": "office", "number": "805-239-3310", "primary": true}], "slogan": "", "address": {"city": "PASO ROBLES", "state_code": "CA"}, "mls_set": "O-MRCA-PRREMAX", "advertiser_id": 2906294, "mls_membership": {"member": {"office_system_id": "PRREMAX"}}}, "photos": [{"href": "https://ap.rdcpix.com/817558233/a0f43de94f42fc34d1b3950c091fedeel-m0x.jpg", "tags": [{"label": "exterior", "probability": 0.832}, {"label": "street_view", "probability": 0.152}, {"label": "unknown", "probability": 0.007}], "description": ""}, {"href": "https://ap.rdcpix.com/879816734/a0f43de94f42fc34d1b3950c091fedeel-m1x.jpg", "tags": [{"label": "exterior", "probability": 0.982}, {"label": "street_view", "probability": 0.015}, {"label": "swimming_pool", "probability": 0.003}], "description": ""}], "address": {"lat": 35.738945, "lon": -120.881253, "city": "Paso Robles", "line": "3675 Delaney Pl", "state": "California", "county": "San Luis Obispo", "fips_code": "06079", "time_zone": "America/Los_Angeles", "state_code": "CA", "postal_code": "93446", "address_validation_code": "121"}, "schools": [{"id": "078812231", "lat": 35.743, "lon": -120.878, "name": "Cappy Culver Elementary School", "phone": "(805) 227-1040", "grades": {"range": {"low": "PK", "high": "8"}}, "nces_id": "063501011786", "ratings": {"parent_rating": 5, "great_schools_rating": 6}, "location": {"city": "Paso Robles", "state": "CA", "county": "San Luis Obispo", "street": "11011 Heritage Ranch Loop Road", "postal_code": "93446"}, "relevance": "assigned", "funding_type": "public", "student_count": 256, "greatschools_id": "0616857", "education_levels": ["elementary", "middle"], "distance_in_miles": 0.3, "student_teacher_ratio": 18.6}, {"id": "078668601", "lat": 35.6167, "lon": -120.671, "name": "Paso Robles High School", "phone": "(805) 769-1500", "grades": {"range": {"low": "9", "high": "12"}}, "nces_id": "060004807404", "ratings": {"parent_rating": 4, "great_schools_rating": 8}, "location": {"city": "Paso Robles", "state": "CA", "county": "San Luis Obispo", "street": "801 Niblick Road", "postal_code": "93446"}, "relevance": "assigned", "funding_type": "public", "student_count": 2034, "greatschools_id": "0606802", "education_levels": ["high"], "distance_in_miles": 14.5, "student_teacher_ratio": 23.4}], "stories": null, "branding": {"listing_agent": {"details": {"link": "/realestateagents/Cristina-Sirotta_Paso-Robles_CA_597675_267009297", "name": "Cristina Sirotta", "phone": null, "photo": null, "slogan": null, "accent_color": null, "show_realtor_logo": true}, "photo_attribution": {"link": null, "name": "Cristina Sirotta", "phone": null, "photo": null, "slogan": null, "accent_color": null, "show_realtor_logo": false}}, "listing_office": {"details": {"link": "WWW.PARKSIDEREALTORS.COM", "name": "Re/Max Parkside Real Estate", "phone": "(805) 239-3310", "photo": null, "slogan": null, "accent_color": null, "show_realtor_logo": false}, "photo_attribution": {"link": null, "name": "Re/Max Parkside Real Estate", "phone": null, "photo": null, "slogan": null, "accent_color": null, "show_realtor_logo": false}}}, "features": [{"text": ["Lake", "Lake Privileges"], "category": "Waterfront and Water Access", "parent_category": "Exterior"}, {"text": ["Lot Description: 0-1 Unit/Acre", "Lot Size Acres: 0.6986", "Lot Size Dimensions: 30, 429", "Lot Size Source: Assessor"], "category": "Land Info", "parent_category": "Exterior"}, {"text": ["View: Canyon, Hills, Lake, Mountain(s), Neighborhood, Panoramic, Trees/Woods", "Lot Size Square Feet: 30429"], "category": "Exterior and Lot Features", "parent_category": "Exterior"}, {"text": ["Association Fee: 285", "Association Fee Frequency: Quarterly", "Association: Yes", "Calculated Total Monthly Association Fees: 95"], "category": "Homeowners Association", "parent_category": "Community"}, {"text": ["Community Features: BLM/National Forest, Curbs, Foothills, Horse Trails, Stable(s)"], "category": "Amenities and Community Features", "parent_category": "Community"}, {"text": ["Source Listing Status: Active", "County: San Luis Obispo", "Directions: G14 to", "Source Property Type: Land/Lot", "Area: PRNW - PR North 46-West 101", "Source Neighborhood: PR Lake Nacimiento(230)", "Parcel Number: 012193019", "Postal Code Plus 4: 7757", "Subdivision: PR Lake Nacimiento(230)", "Zoning: RSF", "Source System Name: C2C"], "category": "Other Property Info", "parent_category": "Listing"}, {"text": ["Sewer: Septic Type Unknown", "Water Source: Private"], "category": "Utilities", "parent_category": "Features"}, {"text": ["HOA Frequency: Monthly/95", "HOA fee: $95"], "category": "Legal and finance"}], "lot_size": {"size": 30431, "units": "sqft"}, "mortgage": {"estimate": {"rate": 4.232, "term": 30, "hoa_fees": 95, "loan_amount": 59600, "down_payment": 14900, "total_payment": 105325, "monthly_payment": 484, "monthly_home_insurance": 19, "monthly_property_taxes": 78, "principal_and_interest": 293, "monthly_mortgage_insurance": 0}, "rates_url": "https://www.realtor.com/mortgage/rates/?from=mobile#zip=93446&property_price=74500&mlid=616843964"}, "products": ["core.agent", "basic_opt_in", "co_broke", "suppress_foreclosure"], "list_date": "2018-09-14T22:43:50Z", "prop_type": "land", "lead_forms": {"form": {"name": {"required": true, "minimum_character_count": 1}, "show": true, "email": {"required": true, "minimum_character_count": 5}, "phone": {"required": true, "maximum_character_count": 11, "minimum_character_count": 10}, "message": {"required": false, "minimum_character_count": 0}}, "form_type": "classic", "lead_type": "co_broke", "show_agent": false, "show_broker": false, "show_builder": false, "is_lcm_enabled": false, "show_veterans_united": false, "show_contact_a_lender": false, "flip_the_market_enabled": false}, "listing_id": "616843964", "year_built": null, "description": "Beautiful views of Nacimiento lake and majestic oaks surround this lovely property in Heritage Ranch. Bring your architect and start designing that dream home. This property accessed by an easement directly behind 3665 Delaney Pl. Very secluded and in a gated community in the newer area. Near market and school.", "last_update": "2019-01-11T11:59:05Z", "photo_count": 2, "prop_status": "for_sale", "property_id": "M1000381744", "rdc_app_url": "move-rdc://www.realtor.com/realestateandhomes-detail/3675-Delaney-Pl_Paso-Robles_CA_93446_M10003-81744", "rdc_web_url": "https://www.realtor.com/realestateandhomes-detail/3675-Delaney-Pl_Paso-Robles_CA_93446_M10003-81744", "tax_history": [{"tax": 797, "year": "2018", "assessment": {"land": 61002, "total": 61002, "building": 0}}, {"tax": 784, "year": "2017", "assessment": {"land": 59806, "total": 59806, "building": 0}}, {"tax": 754, "year": "2016", "assessment": {"land": 58634, "total": 58634, "building": 0}}, {"tax": 744, "year": "2015", "assessment": {"land": 57754, "total": 57754, "building": 0}}, {"tax": 721, "year": "2014", "assessment": {"land": 56623, "total": 56623, "building": 0}}, {"tax": 651, "year": "2013", "assessment": {"land": 50000, "total": 106368, "building": 56368}}, {"tax": 651, "year": "2012", "assessment": {"land": 50000, "total": 105263, "building": 55263}}, {"tax": 650, "year": "2011", "assessment": {"land": 50000, "total": 50000, "building": 0}}, {"tax": 753, "year": "2010", "assessment": null}, {"tax": 1171, "year": "2009", "assessment": {"land": 60000, "total": 60000, "building": 0}}, {"tax": 2117, "year": "2008", "assessment": null}], "feature_tags": ["community_security_features", "hill_or_mountain_view", "lake_view", "view", "water_view", "waterfront", "gated_community", "ranch"], "sold_history": [{"date": "2010-10-07T07:00:00Z", "source": "public record", "listing": {"price": 30000}}, {"date": "2005-07-29T07:00:00Z", "source": "public record", "listing": {"price": 1099000}}], "building_size": null, "listing_status": "Active", "public_records": [{"beds": null, "pool": null, "sqft": null, "view": null, "baths": null, "cl_id": "A5778EB2E693E248EB0B50954F8C3A64", "rooms": null, "style": null, "units": null, "garage": null, "cooling": "Unknown", "heating": "Unknown", "roofing": null, "stories": null, "lot_size": 30429, "exterior1": null, "exterior2": null, "fireplace": null, "prop_type": "land", "year_built": null, "construction": null, "date_updated": "11/30/2018", "garage_spaces": null, "distinct_baths": null, "year_renovated": null}], "detail_tracking": "type|property|data|prop_id|1000381744|list_id|616843964|address|city|Paso+Robles|state|CA|postal|93446|neighborhood|county|San+Luis+Obispo|mls|id|NS18223217|abbr|MRCA|price|detail_branding|listing_agent|listing_office|data_source|advertiser_id|agent|office|property_status|product_code|advantage_code^1LHG|4AV5|38XT|CT63|1QAIE|35T|I|1^^$0|1|2|$3|4|5|6|7|$8|9|A|B|C|D|E|-5|F|G]|H|$I|J|K|L]|M|X|N|$O|Y|P|Z]|Q|H|R|$S|10|T|11]|U|12|V|13|W|14]]", "data_source_name": "mls", "property_history": [{"date": "2018-09-11T17:00:00Z", "sqft": 0, "price": 74500, "source": "MLS #NS18223217", "event_name": "Listed", "price_changed": 0, "datasource_name": "CRMLS", "price_range_max": null, "price_range_min": null}, {"date": "2010-10-07T17:00:00Z", "sqft": 0, "price": 30000, "source": "Public Record", "event_name": "Sold", "price_changed": 0, "datasource_name": "", "price_range_max": null, "price_range_min": null}, {"date": "2005-07-29T17:00:00Z", "sqft": 0, "price": 1099000, "source": "Public Record", "event_name": "Sold", "price_changed": 0, "datasource_name": "", "price_range_max": null, "price_range_min": null}], "photo_attribution": ["Presented by Cristina Sirotta with Re/Max Parkside Real Estate"], "client_display_flags": {"is_turbo": false, "is_new_plan": false, "is_showcase": false, "price_change": 0, "is_short_sale": false, "has_open_house": false, "is_foreclosure": false, "is_new_listing": false, "suppress_map_pin": false, "is_co_broke_email": true, "is_co_broke_phone": false, "is_new_construction": false, "presentation_status": "for_sale", "lead_form_phone_required": true, "is_office_standard_listing": false, "is_showcase_choice_enabled": false, "show_veterans_united_in_lead_form": false, "show_contact_a_lender_in_lead_form": false}}]}'
print(len(json_data))

#
# print(len(compress_data))
# decompress_data = zlib.decompress(compress_data)
# decompress_data_decode = decompress_data.decode()
# print(decompress_data_decode ==json_data )




# 0.03602266311645508
# 0.01501011848449707


# 三种测试方式：测试数据量必须要大

# 1：未作处理直接上传送的情况
# 2通过requests自带的zip压缩（headers中设置）
# 3 通过compress 压缩 来测试


test_data = ''

def no_process_post():

    time_now = time.time()
    requests.post(url='http://127.0.0.1:5000/test_compress_data_post/',
                  # data = compress_data,
                  json=json_data)
    print(time.time() - time_now)


def add_zip_header_post():
    headers = {'Content-type': 'application/json',
               'Accept-Encoding': 'gzip'}
    time_now = time.time()
    requests.post(url='http://127.0.0.1:5000/test_compress_data_post/',
                  # data = compress_data,
                  json=json_data, headers=headers)
    print(time.time() - time_now)


def zip_by_compress():
    print(len(json_data))
    print('strip',len(json_data.strip()))
    json_data_encode = json_data.encode()
    print(len(json_data_encode))

    compress_data = zlib.compress(json_data_encode)
    print(type(compress_data))
    print(len(compress_data))

    # time_now = time.time()
    # requests.post(url='http://127.0.0.1:5000/test_compress_data_post/',
    #               # data = compress_data,
    #               json=json_data)
    # print(time.time() - time_now)


if __name__ == '__main__':
    # no_process_post()
    # add_zip_header_post()
    # zip_by_compress()

    a = 'aaaa aaa'
    print(len(a))
    print(len(a.strip()))