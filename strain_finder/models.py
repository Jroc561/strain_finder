import pandas as pd
import numpy as np

flavors = ['earthy', 'tree_fruit', 'pine', 'vanilla', 'sweet', 'chestnut', 'apricot', 'apple', 
            'skunk', 'grape', 'diesel', 'lime', 'honey', 'pungent', 'violet', 'menthol', 'chemical', 'cheese',
            'mango', 'orange', 'lavender', 'plum', 'citrus', 'tar', 'spicy_herbal', 'minty', 'butter', 
            'peach', 'nutty', 'mint', 'berry', 'ammonia', 'pear', 'rose', 'pineapple', 'blue_cheese', 'tea', 
            'flowery', 'strawberry', 'grapefruit', 'sage', 'blueberry', 'woody', 'tobacco', 'tropical', 
            'pepper', 'coffee', 'lemon']

effects = ['giggly', 'paranoid', 'uplifted', 'aroused', 'horny', 'sleepy', 'talkative', 'hungry', 
            'tingly', 'energetic', 'relaxed', 'focused', 'dry_mouth', 'creative', 'euphoric', 'happy', 
            'anxious']

ailments = ['insomnia', 'lack_of_appetite', 'stress', 'nausea', 'pain', 'inflammation', 'depression', 
            'muscle_spasms']

categories = ['crumble', 'pre-roll', 'drink', 'bath', 'soup', 'spread', 'wax', 'vape_cartidge', 
            'snack', 'kief', 'candy', 'bubble_hash', 'vapes', 'pill', 'tincture', 'dressing', 'salt', 
            'chocolate', 'disposable_vape', 'oil', 'concentrate', 'rso', 'shatter', 'topical', 'edibles', 
            'flowers']

columns = ['flavor_earthy',
 'flavor_pine',
 'flavor_vanilla',
 'flavor_sweet',
 'flavor_chestnut',
 'flavor_apricot',
 'flavor_apple',
 'flavor_skunk',
 'flavor_grape',
 'flavor_none',
 'flavor_diesel',
 'flavor_lime',
 'flavor_honey',
 'flavor_pungent',
 'flavor_violet',
 'flavor_menthol',
 'flavor_chemical',
 'flavor_cheese',
 'flavor_mango',
 'flavor_orange',
 'flavor_lavender',
 'flavor_plum',
 'flavor_citrus',
 'flavor_tar',
 'flavor_spicy_herbal',
 'flavor_minty',
 'flavor_butter',
 'flavor_peach',
 'flavor_nutty',
 'flavor_mint',
 'flavor_berry',
 'flavor_ammonia',
 'flavor_pear',
 'flavor_rose',
 'flavor_pineapple',
 'flavor_tea',
 'flavor_flowery',
 'flavor_strawberry',
 'flavor_grapefruit',
 'flavor_sage',
 'flavor_blueberry',
 'flavor_woody',
 'flavor_tobacco',
 'flavor_tropical',
 'flavor_pepper',
 'flavor_coffee',
 'flavor_lemon',
 'flavor_tree_fruit',
 'flavor_blue_cheese',
 'effect_giggly',
 'effect_paranoid',
 'effect_uplifted',
 'effect_mouth',
 'effect_aroused',
 'effect_horny',
 'effect_sleepy',
 'effect_dry',
 'effect_talkative',
 'effect_none',
 'effect_hungry',
 'effect_tingly',
 'effect_energetic',
 'effect_relaxed',
 'effect_focused',
 'effect_dry_mouth',
 'effect_creative',
 'effect_euphoric',
 'effect_happy',
 'effect_anxious',
 'ailment_insomnia',
 'ailment_lack_of_appetite',
 'ailment_stress',
 'ailment_nausea',
 'ailment_pain',
 'ailment_inflammation',
 'ailment_depression',
 'ailment_muscle_spasms',
 'category_crumble',
 'category_pre-roll',
 'category_drink',
 'category_bath',
 'category_soup',
 'category_spread',
 'category_wax',
 'category_vape_cartidge',
 'category_snack',
 'category_kief',
 'category_candy',
 'category_bubble_hash',
 'category_vapes',
 'category_pill',
 'category_tincture',
 'category_dressing',
 'category_salt',
 'category_chocolate',
 'category_disposable_vape',
 'category_oil',
 'category_concentrate',
 'category_rso',
 'category_shatter',
 'category_topical',
 'category_edibles',
 'category_flowers']





