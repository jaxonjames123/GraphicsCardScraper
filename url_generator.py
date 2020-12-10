# Amazon.com base urls = https://www.amazon.com/{model}/dp/{model_num}
amazon_cards = {'ZOTAC-Graphics-IceStorm-Advanced-ZT-A30800D-10P': ['B08HJNKT3P',
                                                                    'B08HVV2P4Z'],
                'ASUS-Graphics-DisplayPort-Military-Grade-Certification': ['B08HH5WF97',
                                                                           'B08HHDP9DW'],
                'Gigabyte-GeForce-Graphics-GV-N3080AORUS-M-10GD': ['B08KJ3VKLQ'],
                'MSI-GeForce-RTX-3080-10G': ['B08HR5SXPS',
                                             'B08HR7SV3M'],
                'EVGA-10G-P5-3897-KR-GeForce-Technology-Backplate': ['B08HR3Y5GQ'],
                'EVGA-10G-P5-3881-KR-GeForce-GAMING-Cooling': ['B08HR6FMF3'],
                'EVGA-10G-P5-3885-KR-GeForce-Cooling-Backplate': ['B08HR55YB5'],
                }


def url_gen():
    urls = []
    # All know urls for amazon
    for card in amazon_cards:
        for model_number in amazon_cards.get(card):
            urls.append(f'https://www.amazon.com/{card}/dp/{model_number}/')
    return urls