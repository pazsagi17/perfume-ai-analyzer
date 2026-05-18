import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 1. Official 200 Verified Real-World Perfume Database with Pyramid Architecture (Top | Mid | Base)
def load_verified_perfumes():
    data = [
        # --- VERSACE ---
        {"name": "Versace Eros", "brand": "Versace", "pyramid": "mint green_apple lemon | tonka_bean ambroxan geranium | vanilla cedar vetiver oakmoss"},
        {"name": "Versace Eros Flame", "brand": "Versace", "pyramid": "chinotto lemon mandarin_orange black_pepper rosemary | rose geranium | cedar patchouli tonka_bean vanilla sandalwood oakmoss"},
        {"name": "Versace Dylan Blue", "brand": "Versace", "pyramid": "bergamot grapefruit water_notes fig_leaf | pepper ambroxan patchouli papyrus violet_leaf | incense musk tonka_bean saffron"},
        {"name": "Versace Pour Homme", "brand": "Versace", "pyramid": "lemon neroli bergamot rose_de_mai | hyacinth clary_sage cedar geranium | tonka_bean musk amber"},
        {"name": "Versace Crystal Noir", "brand": "Versace", "pyramid": "pepper ginger cardamom | coconut gardenia orange_blossom peony | sandalwood musk amber"},
        {"name": "Versace Man Eau Fraiche", "brand": "Versace", "pyramid": "lemon bergamot carambola cardamom rosewood | cedar tarragon sage pepper | musk saffron amber woody_notes"},
        {"name": "Versace Blue Jeans", "brand": "Versace", "pyramid": "citruses bergamot juniper anise rosewood | lavender jasmine sage lily-of-the-valley | vanilla tonka_bean sandalwood amber musk cedar oakmoss"},
        {"name": "Versace The Dreamer", "brand": "Versace", "pyramid": "lavender mandarin_orange sage | floral_notes tobacco rose | amber tarragon cedar tonka_bean fir"},
        {"name": "Versace Bright Crystal", "brand": "Versace", "pyramid": "yuzu pomegranate water_notes | peony lotus magnolia | musk mahogany amber"},
        {"name": "Versace Yellow Diamond", "brand": "Versace", "pyramid": "amalfi_lemon pear bergamot neroli | mimosa freesia osmanthus orange_blossom | musk guaiac_wood amber"},

        # --- XERJOFF ---
        {"name": "Xerjoff Naxos", "brand": "Xerjoff", "pyramid": "lavender bergamot lemon | honey cinnamon cashmere_wood jasmine | tobacco_leaf vanilla tonka_bean"},
        {"name": "Xerjoff Erba Pura", "brand": "Xerjoff", "pyramid": "orange lemon bergamot | fruity_notes | vanilla white_musk amber"},
        {"name": "Xerjoff Alexandria II", "brand": "Xerjoff", "pyramid": "rosewood lavender cinnamon apple | rose cedar lily-of-the-valley | oud sandalwood vanilla amber musk"},
        {"name": "Xerjoff Lira", "brand": "Xerjoff", "pyramid": "blood_orange bergamot lavender | caramel cinnamon jasmine licorice | musk vanilla"},
        {"name": "Xerjoff Accento", "brand": "Xerjoff", "pyramid": "pineapple hyacinth | iris jasmine pink_pepper | musk amber vetiver patchouli vanilla"},
        {"name": "Xerjoff Mefisto", "brand": "Xerjoff", "pyramid": "grapefruit bergamot lemon | lavender iris rose | musk cedar sandalwood amber"},
        {"name": "Xerjoff Renaissance", "brand": "Xerjoff", "pyramid": "petitgrain bergamot amalfi_lemon mandarin_orange | mint lily-of-the-valley rose | amber musk cedar patchouli"},
        {"name": "Xerjoff Uden", "brand": "Xerjoff", "pyramid": "citruses lemon bergamot | rose guaiac_wood rum coffee | vanilla absolute_musk ambergris"},
        {"name": "Xerjoff Cruz del Sur II", "brand": "Xerjoff", "pyramid": "mango pineapple apple_blossom guava | exotic_floral_notes violet_leaf leaf_notes milk | dried_fruits musk cedar vetyver"},
        {"name": "Xerjoff Tony Iommi Monkey Special", "brand": "Xerjoff", "pyramid": "rum passionfruit bergamot geranium | cinnamon leather patchouli bulgarian_rose | labdanum caramel vanilla tonka_bean sandalwood musk ambergris"},

        # --- PARFUMS DE MARLY ---
        {"name": "Parfums de Marly Layton", "brand": "Parfums de Marly", "pyramid": "apple lavender bergamot mandarin_orange | geranium violet jasmine | vanilla cardamom sandalwood pepper"},
        {"name": "Parfums de Marly Herod", "brand": "Parfums de Marly", "pyramid": "cinnamon pepper | tobacco_leaf incense osmanthus labdanum | vanilla cedar vetiver musk"},
        {"name": "Parfums de Marly Oajan", "brand": "Parfums de Marly", "pyramid": "cinnamon honey osmanthus | benzoin labdanum artemisia | ambergris vanilla tonka_bean patchouli musk"},
        {"name": "Parfums de Marly Greenley", "brand": "Parfums de Marly", "pyramid": "green_apple bergamot mandarin_orange | cashmere_wood cedar violet pomarose | oakmoss musk amberwood"},
        {"name": "Parfums de Marly Sedley", "brand": "Parfums de Marly", "pyramid": "lemon mint bergamot grapefruit mandarin_orange | lavender rosemary geranium olibanum | patchouli cedar vetiver ambroxan sandalwood"},
        {"name": "Parfums de Marly Percival", "brand": "Parfums de Marly", "pyramid": "lavender mandarin_orange bergamot geranium | coriander cinnamon violet jasmine | musk amberwood ambroxan cedar fir"},
        {"name": "Parfums de Marly Pegasus", "brand": "Parfums de Marly", "pyramid": "heliotrope cumin bergamot | bitter_almond lavender jasmine | vanilla sandalwood amber"},
        {"name": "Parfums de Marly Carlisle", "brand": "Parfums de Marly", "pyramid": "nutmeg green_apple saffron | tonka_bean rose osmanthus davana | patchouli vanilla opoponax"},
        {"name": "Parfums de Marly Haltane", "brand": "Parfums de Marly", "pyramid": "clary_sage lavender bergamot | saffron praline | oud cedarwood elderwood musk leather patchouli"},
        {"name": "Parfums de Marly Delina", "brand": "Parfums de Marly", "pyramid": "litchi rhubarb bergamot nutmeg | turkish_rose peony musk vanilla | cashmere_wood cedar vetiver incense"},

        # --- TOM FORD ---
        {"name": "Tom Ford Lost Cherry", "brand": "Tom Ford", "pyramid": "bitter_almond black_cherry cherry_liqueur plum | turkish_rose jasmine_sambac | tonka_bean vanilla cinnamon cloves cedar patchouli vetiver"},
        {"name": "Tom Ford Tobacco Vanille", "brand": "Tom Ford", "pyramid": "tobacco_leaf spicy_notes | vanilla cacao tonka_bean tobacco_blossom | dried_fruits woody_notes"},
        {"name": "Tom Ford Oud Wood", "brand": "Tom Ford", "pyramid": "cardamom sichuan_pepper rosewood | agarwood oud sandalwood vetiver | tonka_bean vanilla amber"},
        {"name": "Tom Ford Noir Extreme", "brand": "Tom Ford", "pyramid": "cardamom nutmeg saffron mandarin_orange neroli | kulfi rose jasmine orange_blossom | vanilla amber sandalwood"},
        {"name": "Tom Ford Ombre Leather", "brand": "Tom Ford", "pyramid": "cardamom | jasmine_sambac leather | patchouli amber moss"},
        {"name": "Tom Ford Black Orchid", "brand": "Tom Ford", "pyramid": "truffle gardenia blackcurrant ylang-ylang jasmine bergamot mandarin_orange amalfi_lemon | orchid spices fruity_notes lotus | patchouli Mexican_chocolate vanilla incense amber sandalwood vetiver white_musk"},
        {"name": "Tom Ford Bitter Peach", "brand": "Tom Ford", "pyramid": "peach blood_orange cardamom heliotrope | rum cognac davana jasmine | patchouli vanilla tonka_bean sandalwood benzoin cashmeran labdanum vetiver"},
        {"name": "Tom Ford Grey Vetiver", "brand": "Tom Ford", "pyramid": "grapefruit orange_blossom_sage | nutmeg orris_root pimento | vetiver woody_notes oakmoss amber"},
        {"name": "Tom Ford Tuscan Leather", "brand": "Tom Ford", "pyramid": "raspberry saffron thyme | olibanum jasmine | leather suede woody_notes amber"},
        {"name": "Tom Ford Soleil Blanc", "brand": "Tom Ford", "pyramid": "pistachio bergamot cardamom pink_pepper | tuberose ylang-ylang jasmine | coconut amber vanilla tonka_bean benzoin"},

        # --- CREED ---
        {"name": "Creed Aventus", "brand": "Creed", "pyramid": "pineapple bergamot apple blackcurrant | birch patchouli jasmine | musk oakmoss vanilla ambergris"},
        {"name": "Creed Green Irish Tweed", "brand": "Creed", "pyramid": "lemon_verbena iris | violet_leaf | ambergris sandalwood"},
        {"name": "Creed Silver Mountain Water", "brand": "Creed", "pyramid": "bergamot mandarin_orange | green_tea blackcurrant | musk sandalwood galbanum petitgrain"},
        {"name": "Creed Millesime Imperial", "brand": "Creed", "pyramid": "fruity_notes sea_salt | sicilian_lemon bergamot mandarin_orange iris | marine_notes woody_notes musk amber"},
        {"name": "Creed Virgin Island Water", "brand": "Creed", "pyramid": "coconut lime white_bergamot sicilian_mandarin | ginger indian_jasmine hibiscus ylang-ylang | sugar_cane white_rum musk"},
        {"name": "Creed Viking", "brand": "Creed", "pyramid": "pink_pepper spicy_mint bergamot lemon absinthe orange | lavender rose clove allspice | sandalwood vetiver patchouli cedar"},
        {"name": "Creed Original Santal", "brand": "Creed", "pyramid": "cinnamon coriander juniper_berries ginger | sandalwood lavender rosemary orange_tree_leaf | tonka_bean vanilla"},
        {"name": "Creed Himalaya", "brand": "Creed", "pyramid": "calabrian_bergamot grapefruit sicilian_lemon mandarin_orange | gunpowder cedar sandalwood | vetiver musk ambergris"},

        # --- DIOR ---
        {"name": "Dior Sauvage", "brand": "Dior", "pyramid": "bergamot pepper | lavender vetiver patchouli | cedar ambroxan"},
        {"name": "Dior Sauvage Elixir", "brand": "Dior", "pyramid": "grapefruit nutmeg cinnamon cardamom | lavender licorice | sandalwood amber patchouli vetiver"},
        {"name": "Dior Homme Intense", "brand": "Dior", "pyramid": "lavender | iris ambrette pear | cedar vetiver"},
        {"name": "Dior Fahrenheit", "brand": "Dior", "pyramid": "lavender mandarin_orange hawthorn nutmeg cedar bergamot chamomile lemon | nutmeg violet_leaf honeysuckle jasmine lily-of-the-valley sandalwood | leather amber patchouli musk vetiver"},
        {"name": "Dior Homme 2020", "brand": "Dior", "pyramid": "bergamot pink_pepper elemi | cashmere_wood atlas_cedar patchouli | iso_e_super haitian_vetiver musk"},
        {"name": "Dior J'adore", "brand": "Dior", "pyramid": "pear melon magnolia peach mandarin_orange bergamot | jasmine lily-of-the-valley tuberose freesia rose orchid plum | musk vanilla blackberry cedarwood"},
        {"name": "Dior Hypnotic Poison", "brand": "Dior", "pyramid": "coconut plum apricot pimento | jasmine lily-of-the-valley rose brazilian_rosewood caraway | sandalwood almond vanilla musk"},
        {"name": "Dior Poison Girl", "brand": "Dior", "pyramid": "bitter_orange lemon | damask_rose grasse_rose | tonka_bean vanilla almond tolu_balsam heliotrope cashmeran sandalwood"},

        # --- CHANEL ---
        {"name": "Bleu de Chanel", "brand": "Chanel", "pyramid": "grapefruit lemon mint nutmeg ginger | jasmine cedar | sandalwood patchouli labdanum incense"},
        {"name": "Coco Mademoiselle", "brand": "Chanel", "pyramid": "orange mandarin_orange bergamot orange_blossom | rose jasmine | patchouli musk vanilla vetiver tonka_bean"},
        {"name": "Chanel No 5", "brand": "Chanel", "pyramid": "aldehydes ylang-ylang neroli bergamot lemon | iris jasmine rose orris_root | vetiver sandalwood patchouli amber musk vanilla oakmoss"},
        {"name": "Chanel Allure Homme Sport", "brand": "Chanel", "pyramid": "orange blood_mandarin sea_notes aldehydes | pepper neroli cedar | vetiver tonka_bean white_musk amber vanilla elemi resin"},
        {"name": "Chanel Platinum Egoiste", "brand": "Chanel", "pyramid": "lavender rosemary neroli petitgrain | geranium clary_sage galbanum jasmine | oakmoss sandalwood vetiver cedar amber"},

        # --- JEAN PAUL GAULTIER ---
        {"name": "JPG Scandal Pour Homme", "brand": "Jean Paul Gaultier", "pyramid": "clary_sage mandarin_orange | caramel | tonka_bean vetiver"},
        {"name": "JPG Scandal", "brand": "Jean Paul Gaultier", "pyramid": "mandarin_orange blood_orange | honey gardenia jasmine orange_blossom peach | caramel licorice beeswax patchouli"},
        {"name": "JPG Le Male", "brand": "Jean Paul Gaultier", "pyramid": "lavender mint cardamom bergamot artemisia | cinnamon orange_blossom caraway | vanilla tonka_bean amber sandalwood cedar"},
        {"name": "JPG Ultra Male", "brand": "Jean Paul Gaultier", "pyramid": "pear lavender mint bergamot lemon | cinnamon caraway clary_sage | black_vanilla amber patchouli cedar"},
        {"name": "JPG Le Male Elixir", "brand": "Jean Paul Gaultier", "pyramid": "lavender mint | vanilla benzoin | honey tonka_bean tobacco"},
        {"name": "JPG Le Beau", "brand": "Jean Paul Gaultier", "pyramid": "bergamot | coconut | tonka_bean woody_notes"},
        {"name": "JPG Le Beau Le Parfum", "brand": "Jean Paul Gaultier", "pyramid": "pineapple iris cypress ginger | coconut woody_notes | tonka_bean sandalwood ambergris amber"},

        # --- PACO RABANNE ---
        {"name": "Paco Rabanne One Million", "brand": "Paco Rabanne", "pyramid": "blood_mandarin mint grapefruit | rose cinnamon spicy_notes | leather amber woody_notes patchouli"},
        {"name": "Paco Rabanne Invictus", "brand": "Paco Rabanne", "pyramid": "sea_notes grapefruit mandarin_orange | bay_leaf jasmine | ambergris guaiac_wood oakmoss patchouli"},
        {"name": "Paco Rabanne One Million Lucky", "brand": "Paco Rabanne", "pyramid": "plum ozonic_notes grapefruit bergamot | hazelnut honey cedar cashmere_wood jasmine orange_blossom | amberwood vanilla patchouli oakmoss"},
        {"name": "Paco Rabanne Olympea", "brand": "Paco Rabanne", "pyramid": "water_jasmine green_mandarin ginger_flower | salt vanilla | ambergris cashmere_wood sandalwood"},

        # --- GIORGIO ARMANI ---
        {"name": "Acqua Di Gio", "brand": "Giorgio Armani", "pyramid": "lime lemon bergamot jasmine orange mandarin_orange neroli | sea_notes freesia rosemary cyclamen violet coriander nutmeg rose persimmon | cedar patchouli oakmoss amber musk"},
        {"name": "Acqua Di Gio Profondo", "brand": "Giorgio Armani", "pyramid": "sea_notes aquozone green_mandarin bergamot | rosemary lavender cypress mastic | patchouli musk amber mineral_notes"},
        {"name": "Stronger With You", "brand": "Giorgio Armani", "pyramid": "cardamom pink_pepper mint violet_leaf | pineapple cinnamon melon sage | lavender vanilla chestnut amberwood cedar guaiac_wood"},
        {"name": "Stronger With You Intensely", "brand": "Giorgio Armani", "pyramid": "pink_pepper juniper violet | cinnamon lavender sage toffee | vanilla tonka_bean amber suede"},
        {"name": "Armani Code", "brand": "Giorgio Armani", "pyramid": "lemon bergamot | olive_blossom guaiac_wood | tonka_bean tobacco leather"},
        {"name": "Armani Sì", "brand": "Giorgio Armani", "pyramid": "cassis | may_rose freesia | vanilla patchouli woody_notes ambroxan"},

        # --- YVES SAINT LAURENT ---
        {"name": "YSL La Nuit de L'Homme", "brand": "Yves Saint Laurent", "pyramid": "cardamom bergamot | lavender virginia_cedar | vetiver caraway"},
        {"name": "YSL Y EDP", "brand": "Yves Saint Laurent", "pyramid": "apple ginger bergamot | sage juniper_berries geranium | amberwood tonka_bean cedar vetiver olibanum"},
        {"name": "YSL Y Le Parfum", "brand": "Yves Saint Laurent", "pyramid": "apple aldehydes grapefruit ginger | lavender sage geranium | cedar olibanum tonka_bean patchouli"},
        {"name": "YSL Black Opium", "brand": "Yves Saint Laurent", "pyramid": "pear pink_pepper orange_blossom | coffee jasmine bitter_almond licorice | vanilla patchouli cedar cashmere_wood"},
        {"name": "YSL Libre", "brand": "Yves Saint Laurent", "pyramid": "lavender mandarin_orange blackcurrant petitgrain | jasmine orange_blossom | vanilla cedar ambergris musk"},

        # --- NISHANE ---
        {"name": "Nishane Hacivat", "brand": "Nishane", "pyramid": "pineapple grapefruit bergamot | cedar patchouli jasmine | oakmoss woody_notes"},
        {"name": "Nishane Ani", "brand": "Nishane", "pyramid": "ginger bergamot pink_pepper green_notes | blackcurrant cardamom turkish_rose | vanilla ambergris benzoin cedar patchouli sandalwood musk"},
        {"name": "Nishane Hundred Silent Ways", "brand": "Nishane", "pyramid": "peach mandarin_orange | tuberose gardenia jasmine orris | vanilla sandalwood vetiver"},
        {"name": "Nishane Wulong Cha", "brand": "Nishane", "pyramid": "bergamot orange mandarin_orange litsea_cubeba | oolong_tea nutmeg | mediterranean_musk fig"},

        # --- KILIAN ---
        {"name": "Kilian Angels Share", "brand": "Kilian", "pyramid": "cognac | cinnamon tonka_bean oak praline | vanilla sandalwood"},
        {"name": "Kilian Black Phantom", "brand": "Kilian", "pyramid": "rum | dark_chocolate coffee sugar almond | caramel sandalwood heliotrope"},
        {"name": "Kilian Love Don't Be Shy", "brand": "Kilian", "pyramid": "neroli bergamot pink_pepper coriander | orange_blossom jasmine honeysuckle rose iris | marshmallow vanilla musk caramel labdanum"},

        # --- MAISON FRANCIS KURKDJIAN ---
        {"name": "Baccarat Rouge 540", "brand": "MFK", "pyramid": "saffron jasmine | amberwood ambergris | fir_resin cedar"},
        {"name": "MFK Grand Soir", "brand": "MFK", "pyramid": "spanish_labdanum | siam_benzoin tonka_bean | amber vanilla"},

        # --- MANCERA & MONTALE ---
        {"name": "Mancera Cedrat Boise", "brand": "Mancera", "pyramid": "sicilian_lemon blackcurrant bergamot spicy_notes | fruity_notes patchouli water_jasmine | leather woody_notes oakmoss sandalwood vanilla white_musk"},
        {"name": "Mancera Instant Crush", "brand": "Mancera", "pyramid": "saffron ginger sicilian_bergamot sicilian_mandarin | Moroccan_rose egyptian_jasmine amberwood | indonesian_patchouli_leaf madagascar_vanilla white_musk oakmoss sandalwood"},
        {"name": "Montale Intense Cafe", "brand": "Montale", "pyramid": "floral_notes | rose coffee | vanilla amber white_musk"},
        {"name": "Montale Arabians Tonka", "brand": "Montale", "pyramid": "saffron bergamot | oud bulgarian_rose | sugar tonka_bean cane_sugar white_musk amber"},

        # --- DOLCE & GABBANA ---
        {"name": "D&G Light Blue Intense Homme", "brand": "Dolce & Gabbana", "pyramid": "grapefruit mandarin_orange | sea_water juniper | musk amberwood"},
        {"name": "D&G The One Eau de Parfum", "brand": "Dolce & Gabbana", "pyramid": "grapefruit coriander basil | ginger cardamom orange_blossom | tobacco amber cedar sandalwood"},

        # --- PRADA ---
        {"name": "Prada L'Homme", "brand": "Prada", "pyramid": "neroli black_pepper cardamom carrot_seeds | iris violet geranium mate | patchouli cedar amber sandalwood"},
        {"name": "Prada Luna Rossa Black", "brand": "Prada", "pyramid": "bergamot | angelica patchouli | coumarin amber woody_notes"},

        # --- GUCCI ---
        {"name": "Gucci Guilty Pour Homme", "brand": "Gucci", "pyramid": "lavender amalfi_lemon | orange_blossom african_orange_blossom | cedar patchouli vanilla"},

        # --- AMOUAGE ---
        {"name": "Amouage Reflection Man", "brand": "Amouage", "pyramid": "rosemary pimento rose_de_mai | jasmine neroli orris_root geranium | sandalwood cedar vetiver patchouli"},
        {"name": "Amouage Interlude Man", "brand": "Amouage", "pyramid": "oregano pimento bergamot | incense opoponax amber labdanum | leather agarwood oud patchouli sandalwood oakmoss"}
    ]
    
    extended_pool = [
        ("Chanel", "Allure Homme", "lemon peach ginger mandarin_orange lavender bergamot | pepper patchouli cedar vetiver rose jasmine anise gardenia rosewood | coconut vanilla tonka_bean sandalwood amber musk oakmoss leather"),
        ("Chanel", "Bleu de Chanel Eau de Parfum", "grapefruit lemon mint pink_pepper bergamot coriander aldehydes | ginger nutmeg jasmine melon | incense amber cedar sandalwood patchouli labdanum woody_notes"),
        ("Chanel", "Bleu de Chanel Parfum", "lemon_zest bergamot mint artemisia | lavender pineapple geranium green_notes | cedar sandalwood amberwood tonka_bean iso_e_super"),
        ("Chanel", "No 5 Eau de Parfum", "aldehydes ylang-ylang neroli bergamot peach | iris jasmine rose lily-of-the-valley | sandalwood vanilla oakmoss vetiver patchouli"),
        ("Chanel", "Coco Noir", "grapefruit calabrian_bergamot orange | rose geranium jasmine narcissus peach | patchouli indonesian_sandalwood olibanum white_musk vanilla tonka_bean cloves benzoin"),
        ("Chanel", "Chance Eau Tendre", "quince grapefruit | hyacinth jasmine | musk iris virginia_cedar amber"),
        ("Dior", "Sauvage Parfum", "bergamot mandarin_orange elemi | sandalwood | olibanum vanilla tonka_bean"),
        ("Dior", "Homme 2005", "lavender sage bergamot | iris cacao amber | cardamom patchouli leather vetiver"),
        ("Dior", "Homme Intense 2011", "lavender | iris ambrette pear | virginia_cedar vetiver"),
        ("Dior", "Fahrenheit Le Parfum", "licorice suede sicilian_mandarin | violet_leaf rum coriander | cumin bourbon_vanilla"),
        ("Dior", "Pure Poison", "jasmine orange_blossom bergamot mandarin_orange | gardenia rose | sandalwood white_amber cedar white_musk"),
        ("Dior", "Dune", "rosewood mandarin_orange aldehyde bergamot | peony lily wallflower jasmine rose ylang-ylang | amber sandalwood benzoin oakmoss vanilla patchouli musk"),
        ("Tom Ford", "Oud Wood Intense", "juniper_berries ginger | nutmeg cypress | castoreum agarwood oud"),
        ("Tom Ford", "Tobacco Oud", "tobacco whiskey | spicy_notes cinnamon coriander | agarwood oud patchouli sandalwood amber benzoin vanilla cedar"),
        ("Tom Ford", "Fucking Fabulous", "lavender clary_sage | bitter_almond leather vanilla orris_root | tonka_bean cashmeran amber woody_notes"),
        ("Tom Ford", "Noir de Noir", "saffron | black_rose truffle | patchouli vanilla oud oakmoss"),
        ("Tom Ford", "Costa Azzurra", "driftwood seaweed celery_seeds ambrette cardamom oud | lemon cypress mandarin_orange lavender myrtle artemisia mastic | oakmoss incense vanilla vetiver lentisque amber"),
        ("Tom Ford", "Beau de Jour", "lavender rosemary | oakmoss mint basil geranium | patchouli amber"),
        ("Tom Ford", "Mandarino di Amalfi", "tarragon mint blackcurrant grapefruit lemon basil bergamot | black_pepper coriander orange_blossom clary_sage shiso jasmine | musk vetiver civet amber labdanum"),
        ("Tom Ford", "Ombre Leather 16", "cardamom | jasmine_sambac leather | oakmoss patchouli violet_leaf"),
        ("Creed", "Aventus Cologne", "mandarin_orange ginger pink_pepper | vetiver patchouli sandalwood | musk birch tonka_bean styrax"),
        ("Creed", "Green Irish Tweed 1985", "lemon_verbena iris | violet_leaf | ambergris mysore_sandalwood"),
        ("Creed", "Millésime Impérial", "sea_salt fruity_notes | sicilian_lemon bergamot mandarin_orange iris | marine_notes woody_notes musk amber"),
        ("Creed", "Bois du Portugal", "bergamot | lavender | cedar sandalwood ambergris vetiver"),
        ("Creed", "Erolfa", "lime bergamot melon green_notes lemon violet | caraway herbal_notes ginger jasmine pepper cyclamen | pine_tree_needles nutmeg ambergris musk sandalwood cedar oakmoss"),
        ("Creed", "Royal Oud", "pink_pepper lemon sicilian_bergamot | cedar angelica galbanum | sandalwood agarwood oud musk"),
        ("Creed", "Tabarome", "ginger tangerine | tobacco leaf ginger | leather sandalwood patchouli ambergris musk"),
        ("Creed", "Neroli Sauvage", "bitter_orange bergamot grapefruit lemon | neroli verbena | ambergris"),
        ("Xerjoff", "Mefisto Gentiluomo", "bergamot lavender lemon grapefruit | iris rose violet | musk cedar amber"),
        ("Xerjoff", "Zefiro", "elemi white_wine artemisia bergamot | cardamom cinnamon cloves iris | incense woody_notes honey amber"),
        ("Xerjoff", "More Than Words", "fruity_notes labdanum | oriental_notes woody_notes oud floral_notes | ambergris olibanum resin"),
        ("Xerjoff", "Casamorati Bouquet Ideale", "cinnamon nutmeg | guaiac_wood sandalwood cedar papyrus | vanilla coumarin tonka_bean absolute_musk french_labdanum tobacco_blossom"),
        ("Xerjoff", "Casamorati 1888", "coriander cloves green_pepper saffron | ylang-ylang neroli rose | birch patchouli sandalwood amber"),
        ("Xerjoff", "Komi Parfum", "mandarin_orange elemi artemisia | lavender cedarwood jasmine | patchouli white_musk vanilla tonka_bean"),
        ("Xerjoff", "Dolce Amalfi", "apple saffron quince cardamom | cloves incense | tolu_balsam vanilla tonka_bean cedar musk amber"),
        ("Parfums de Marly", "Pegasus Exclusif", "cardamom heliotrope pink_pepper bergamot | bitter_almond lavender jasmine geranium | oud vanilla sandalwood amber_wood guaiac_wood"),
        ("Parfums de Marly", "Layton Exclusif", "almond mandarin_orange bergamot watery_notes | civet geranium rose gardenia water_lily | oud guaiac_wood patchouli sandalwood amber oakmoss pink_pepper vanilla"),
        ("Parfums de Marly", "Galloway", "citruses pepper | iris orange_blossom | musk amber"),
        ("Parfums de Marly", "Godolphin", "saffron thyme fruity_notes green_notes | cypress mate jasmine rose iris | leather vetiver virginia_cedar amber vanille musk"),
        ("Parfums de Marly", "Kalan", "spices blood_orange black_pepper | lavender orange_blossom | woody_notes moss tonka_bean sandalwood amber"),
        ("Parfums de Marly", "Oriana", "mandarin_orange bergamot grapefruit | orange_blossom raspberry blackcurrant whipped_cream marshmallow | musk ambrette"),
        ("Parfums de Marly", "Athalia", "bitter_orange incense | iris orange_blossom | white_musk amber vanilla"),
        ("Parfums de Marly", "Darley", "mint bergamot amalfi_lemon | lavender cinnamon rose orange_blossom rosemary | tonka_bean sandalwood amber patchouli guaiac_wood"),
        ("Parfums de Marly", "Byerley", "bergamot cardamom | cedarwood guaiac_wood | vetiver resin"),
        ("Yves Saint Laurent", "L'Homme", "ginger bergamot lemon spices | white_pepper basil violet_leaf | tonka_bean tahitian_vetiver cedarwood"),
        ("Yves Saint Laurent", "La Nuit de L'Homme Frozen Cologne", "bergamot mandarin_orange lemon | pepper geranium mint black_pepper | cedar vetiver tonka_bean cashmere_wood"),
        ("Yves Saint Laurent", "La Nuit de L'Homme Le Parfum", "pepper anise bergamot | fruity_notes lavender french_labdanum | vanille patchouli vetiver"),
        ("Yves Saint Laurent", "L'Homme Intense", "lemon bergamot black_pepper | orange_blossom artemisia violet_leaf | ambergris woody_notes cedar suede benzoin leather"),
        ("Yves Saint Laurent", "Tuxedo", "violet_leaf coriander bergamot | rose black_pepper lily-of-the-valley | patchouli ambergris bourbon_vanilla"),
        ("Yves Saint Laurent", "Kouros", "aldehydes artemisia coriander clary_sage bergamot | honey patchouli cinnamon iris jasmine | vetiver cedar oakmoss civet leather musk amber"),
        ("Yves Saint Laurent", "M7 Oud Absolu", "mandarin_orange | patchouli agarwood oud | myrrh french_labdanum"),
        ("Yves Saint Laurent", "Rive Gauche Pour Homme", "rosemary star_anise bergamot | lavender clove geranium | coumarin oakmoss guaiac_wood vetiver patchouli"),
        ("Jean Paul Gaultier", "Le Male Le Parfum", "cardamom | lavender iris | vanilla oriental_notes woody_notes"),
        {"name": "JPG Le Beau Paradise Garden", "brand": "Jean Paul Gaultier", "pyramid": "water_notes green_notes mint ginger | coconut fig | tonka_bean sandalwood absolute_vanilla"},
        {"name": "JPG Scandal Absolu", "brand": "Jean Paul Gaultier", "pyramid": "mirabelle_plum | chestnut sandalwood tuberose | fig honey amber"},
        {"name": "Jean Paul Gaultier Gaultier 2", "brand": "Jean Paul Gaultier", "pyramid": "amber | musk | vanilla"},
        {"name": "Jean Paul Gaultier Fleur du Male", "brand": "Jean Paul Gaultier", "pyramid": "petitgrain | orange_blossom | fern chamomile caraway"},
        {"name": "Jean Paul Gaultier Le Male Aviator", "brand": "Jean Paul Gaultier", "pyramid": "mint | violet_leaf | woody_notes absolute_vanilla"},
        ("Giorgio Armani", "Acqua Di Gio Essenza", "water_notes bergamot grapefruit calone | jasmine floral_notes basil rosemary | cedar patchouli vetiver ambergris pepper amber clary_sage"),
        ("Giorgio Armani", "Acqua Di Gio Profumo", "sea_notes bergamot | rosemary sage geranium | incense patchouli"),
        ("Giorgio Armani", "Armani Code Profumo", "green_mandarin green_apple cardamom | orange_blossom lavender nutmeg | tonka_bean leather amber"),
        ("Giorgio Armani", "Armani Code Colonia", "bergamot mandarin_orange pink_pepper | orange_blossom clary_sage | tonka_bean heliotrope amberwood"),
        ("Giorgio Armani", "Stronger With You Absolute", "rum elemi bergamot | lavender davana chestnut | Madagascar_vanilla cedarwood guaiac_wood patchouli"),
        ("Giorgio Armani", "Stronger With You Freeze", "lime ginger mandarin_orange apple | lavender sage bourbon_geranium | cardamom marron_glace vanilla amberwood guaiac_wood"),
        ("Giorgio Armani", "Sì Passione", "pear blackcurrant pink_pepper grapefruit | rose jasmine heliotrope pineapple | vanilla cedarwood amberwood patchouli lorenox"),
        ("Paco Rabanne", "One Million Privé", "blood_mandarin cinnamon | tobacco_leaf myrrh | tonka_bean patchouli"),
        ("Paco Rabanne", "Invictus Aqua", "grapefruit yuzu pink_pepper | sea_water violet_leaf | ambergris amberwood guaiac_wood"),
        ("Paco Rabanne", "Invictus Victory", "pink_pepper lemon | lavender olibanum | vanilla tonka_bean amber"),
        ("Paco Rabanne", "Phantom Legion", "lavender lemon_zest amalfi_lemon | smoke apple earthy_notes | patchouli vanilla vetiver"),
        ("Paco Rabanne", "Pure XS", "ginger thyme green_notes grapefruit bergamot | vanilla liquor leather cinnamon sugar apple coriander | cedar cashmere_wood patchouli myrrh woody_notes"),
        ("Paco Rabanne", "Black XS", "citruses lemon tagetes sage | praline cinnamon tolu_balsam | black_cardamom rosewood patchouli black_amber ebony_tree"),
        ("Dolce & Gabbana", "The One for Men EDT", "coriander basil grapefruit | ginger cardamom orange_blossom | tobacco amber cedar sandalwood"),
        ("Dolce & Gabbana", "The One Royal Night", "cardamom basil pear_wood | nutmeg cedar_wood | sandalwood amber labdanum"),
        ("Dolce & Gabbana", "The One Mysterious Night", "saffron grapefruit | rose oud clary_sage labdanum | amber tonka_bean precious_woods"),
        ("Dolce & Gabbana", "Light Blue Pour Homme", "grapefruit bergamot sicilian_mandarin | juniper pepper rosemary | rosewood musk incense oakmoss"),
        ("Dolce & Gabbana", "Light Blue Forever Pour Homme", "grapefruit bergamot | ozonic_notes violet_leaf | vetiver oil musk patchouli white_musk"),
        ("Dolce & Gabbana", "K by D&G Eau de Parfum", "blood_orange pimento juniper_berries lemon | cardamome fig_nectar lavender geranium clary_sage | cedar patchouli vetiver nagarmotha base"),
        ("Prada", "L'Homme L'Eau", "neroli ginger | iris amber powdery_notes | sandalwood cedar woody_notes"),
        ("Prada", "L'Homme Intense", "iris amber | leather patchouli | tonka_bean sandalwood"),
        ("Prada", "Luna Rossa", "lavender bitter_orange mint | clary_sage ambrette | musk_mallow ambroxan"),
        ("Prada", "Luna Rossa Carbon", "bergamot pepper | lavender soil_tincture watery_notes metallic_notes | coal ambroxan patchouli"),
        ("Prada", "Luna Rossa Sport", "juniper_berries ginger | lavender | vanilla tonka_bean"),
        ("Prada", "Luna Rossa Ocean", "bergamot pink_pepper artemisia | iris lavender saffron sage | suede vetiver musk caramel patchouli"),
        ("Gucci", "Gucci Guilty Absolute", "leather | patchouli cypress woody_notes | vetiver"),
        ("Gucci", "Gucci Guilty Pour Homme EDP", "rose balsamic_vinegar red_chili_pepper salt | lavender orange_blossom | cedar patchouli"),
        ("Gucci", "Gucci Oud", "pear saffron raspberry | bulgarian_rose orange_blossom | agarwood oud patchouli amber musk"),
        ("Gucci", "Gucci Intense Oud", "incense woody_notes | leather amber | agarwood oud olibanum"),
        ("Gucci", "Envy for Men", "ginger cardamom lavender pepper coriander | mahogany mandarin_orange artemisia cedar sandalwood nutmeg cloves rose jasmine heliotrope | vanilla incense amber tonka_bean patchouli musk leather oakmoss"),
        ("Nishane", "Hacivat X", "pineapple bergamot pink_pepper lime | hibiscus jasmine | cedarwood patchouli vetiver vanilla"),
        ("Nishane", "Fan Your Flames", "coconut rum | tobacco_leaf | tonka_bean oakmoss cedarwood"),
        ("Nishane", "Karagoz", "pineapple herbal_notes grape | neroli jasmine | patchouli vetiver agarwood oud amber"),
        ("Nishane", "Ege / ΑΙΓΑΙΟ", "yuzu violet_leaf anise | basil mint cardamom | lavender licorice olibanum"),
        ("Nishane", "B-612", "lavender cypress geranium | cashmeran cedar sandalwood | patchouli musk oakmoss tonka_bean"),
        ("Nishane", "Pasion Choco", "passionfruit coffee grapefruit | dark_chocolate orchid coriander | patchouli vanilla benzoin black_musk"),
        ("Mancera", "Red Tobacco", "cinnamon saffron nutmeg green_apple white_pear | incense jasmine patchouli_leaf tobacco | vanilla amber sandalwood guaiac_wood white_musk oud"),
        ("Mancera", "Aoud Lemon Mint", "lemon coriander pepper mandarin_orange | jasmine patchouli_leaf egyptian_jasmine | oud leather amber vetiver vanilla white_musk"),
        ("Mancera", "Coco Vanille", "coconut white_peach | tiare_flower ylang-ylang egyptian_jasmine | madagascar_vanilla guaic_wood white_musk"),
        ("Mancera", "Hindu Kush", "incense cannabis spices labdanum | patchouli_leaf amber | white_musk guaiac_wood vanilla_pod"),
        ("Mancera", "Sicily", "mandarin_orange grapefruit peach pineapple bergamot apple | jasmine ylang-ylang rose violet | white_musk woody_notes"),
        ("Montale", "Honey Aoud", "honey | agarwood oud cinnamon amber | vanilla floral_notes leather patchouli"),
        ("Montale", "Roses Vanille", "italian_lemon water_notes | turkish_rose sugar | vanilla white_musk cedar"),
        ("Montale", "Sensual Instinct", "roasted_coffee_beans | rose praline | oakmoss amber"),
        ("Montale", "Starry Nights", "lemon bergamot apple | patchouli bulgarian_rose egyptian_jasmine | powdery_notes white_musk amber"),
        ("Montale", "Black Aoud", "mandarin_orange | rose french_labdanum musk patchouli | agarwood oud"),
        ("Amouage", "Jubilation XXV Man", "blackberry olibanum orange labdanum coriander tarragon | guaiac_wood honey bay_leaf cinnamon orchid rose cloves | opoponax oud patchouli myrrh cedar musk oakmoss ambergris"),
        ("Amouage", "Lyric Man", "lime bergamot | rose angelica ginger orange_blossom nutmeg saffron galbanum | pine_tree incense musk sandalwood vanilla vetiver oakmoss"),
        ("Amouage", "Epic Man", "pink_pepper olibanum nutmeg saffron cardamom caraway | myrrh geranium | oud patchouli leather incense sandalwood cedar musk"),
        ("Amouage", "Beach Hut Man", "mint galbanum orange_blossom | ivy vetiver moss | woody_notes patchouli myrrh"),
        ("Amouage", "Overture Man", "cognac cumin cardamom nutmeg saffron ginger grapefruit | myrrh labdanum cinnamon benzoin geranium mastic | patchouli sandalwood incense leather smoke"),
        ("MFK", "540 Extrait de Parfum", "bitter_almond saffron | egyptian_jasmine cedar | ambergris woody_notes musk"),
        ("MFK", "Aqua Celestia", "lime mint blackcurrant | neroli mimosa green_notes | white_musk"),
        ("MFK", "Amyris Homme", "rosemary mandarin_orange | amyris coconut iris milk_chocolate | coffee oud tonka_bean")
    ]
    
    for item in extended_pool:
        if isinstance(item, dict):
            data.append(item)
        else:
            data.append({"name": item[1], "brand": item[0], "pyramid": item[2]})
            
    return pd.DataFrame(data[:200])

NOTE_CATEGORIES = {
    "Citrus": ["lemon", "bergamot", "mandarin_orange", "orange", "grapefruit", "lime", "neroli", "citruses", "amalfi_lemon", "chinotto", "yuzu", "blood_orange", "tangerine", "calabrian_bergamot", "white_bergamot", "sicilian_mandarin", "lemon_zest", "bitter_orange", "blood_and_orange", "blood_mandarin", "green_mandarin", "sicilian_lemon", "sicilian_bergamot", "lemon_verbena", "litsea_cubeba"],
    "Woody": ["cedar", "sandalwood", "patchouli", "birch", "oakmoss", "vetiver", "ambroxan", "amberwood", "oud", "cashmeran", "ambergris", "agarwood", "rosewood", "cedarwood", "papyrus", "woody_notes", "fir", "fir_resin", "mahogany", "guaiac_wood", "virginia_cedar", "moss", "cashmere_wood", "oak", "driftwood", "seaweed", "cypress", "elderwood", "atlas_cedar", "haitian_vetiver", "indonesian_sandalwood", "mysore_sandalwood", "pine_tree", "pine_tree_needles", "precious_woods", "ebony_tree", "nagarmotha", "iso_e_super", "amber_wood"],
    "Fresh Spicy": ["mint", "nutmeg", "ginger", "pepper", "lavender", "cinnamon", "saffron", "cardamom", "cloves", "pink_pepper", "black_pepper", "sichuan_pepper", "spices", "spicy_notes", "sage", "clary_sage", "rosemary", "caraway", "coriander", "anise", "tarragon", "star_anise", "cumin", "thyme", "oregano", "pimento", "allspice", "black_cardamom", "red_chili_pepper", "white_pepper", "green_pepper", "celery_seeds", "spicy_mint"],
    "Sweet": ["vanilla", "honey", "caramel", "chocolate", "Mexican_chocolate", "dark_chocolate", "praline", "tonka_bean", "cacao", "licorice", "wax", "coffee", "black_vanilla", "amber", "benzoin", "leather", "incense", "tobacco", "tobacco_leaf", "beeswax", "rum", "cognac", "sugar", "kulfi", "bitter_almond", "almond", "toffee", "suede", "myrrh", "olibanum", "opoponax", "labdanum", "spanish_labdanum", "siam_benzoin", "tolu_balsam", "balsamic_vinegar", "smoke", "whiskey", "marshmallow", "whipped_cream", "cane_sugar", "roasted_coffee_beans", "milk_chocolate"],
    "Fruity": ["pineapple", "apple", "green_apple", "blackcurrant", "peach", "coconut", "plum", "apricot", "pear", "black_cherry", "cherry_liqueur", "sour_cherry", "dried_fruits", "melon", "blackberry", "raspberry", "fig", "fruity_notes", "pomegranate", "carambola", "juniper_berries", "fig_leaf", "truffle", "quince", "litchi", "rhubarb", "pomarose", "bitter_peach", "grape", "passionfruit", "mango", "guava", "mirabelle_plum", "chestnut", "marron_glace", "fig_nectar", "cassis", "juniper", "berries"]
}

ALL_UNIQUE_NOTES = sorted(list(set([note for keywords in NOTE_CATEGORIES.values() for note in keywords])))

def format_note_text(raw_notes_string):
    if not raw_notes_string or str(raw_notes_string).strip() == "":
        return "No specific notes available"
    clean_str = str(raw_notes_string).replace('|', ' ')
    formatted_tokens = [token.replace("_", " ").title() for token in clean_str.split()]
    return ", ".join(formatted_tokens)

def calculate_pyramid_profile(pyramid_str):
    parts = str(pyramid_str).split('|')
    top_notes = parts[0].split() if len(parts) > 0 else []
    mid_notes = parts[1].split() if len(parts) > 1 else []
    base_notes = parts[2].split() if len(parts) > 2 else []
    
    counts = {cat: 0.0 for cat in NOTE_CATEGORIES.keys()}
    weights = {"top": 1.0, "mid": 1.2, "base": 1.5}
    
    for note in top_notes:
        for cat, keywords in NOTE_CATEGORIES.items():
            if note.lower() in keywords: counts[cat] += weights["top"]
    for note in mid_notes:
        for cat, keywords in NOTE_CATEGORIES.items():
            if note.lower() in keywords: counts[cat] += weights["mid"]
    for note in base_notes:
        for cat, keywords in NOTE_CATEGORIES.items():
            if note.lower() in keywords: counts[cat] += weights["base"]
            
    total_weight = sum(counts.values())
    if total_weight == 0: return {cat: 0.0 for cat in NOTE_CATEGORIES.keys()}
    return {cat: round((val / total_weight) * 100, 1) for cat, val in counts.items()}

def find_closest_perfume_match(custom_profile, df):
    categories = ["Citrus", "Woody", "Fresh Spicy", "Sweet", "Fruity"]
    custom_vector = np.array([custom_profile[cat] for cat in categories])
    if np.all(custom_vector == 0): return None, 0.0
    best_match_name = None
    best_similarity = -1.0
    for _, row in df.iterrows():
        db_profile = calculate_pyramid_profile(row['pyramid'])
        db_vector = np.array([db_profile[cat] for cat in categories])
        if np.all(db_vector == 0): continue
        similarity = np.dot(custom_vector, db_vector) / (np.linalg.norm(custom_vector) * np.linalg.norm(db_vector))
        if similarity > best_similarity:
            best_similarity = similarity
            best_match_name = row['name']
    return best_match_name, round(best_similarity * 100, 1)

def main():
    # FIXED: Proper injection of custom theme configuration, viewport scaling and PWA requirements
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
        
        /* Premium Background Layout overriding native Streamlit style elements */
        .stApp, html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
            font-family: 'Inter', sans-serif !important;
            background-color: #0b0c10 !important;
            color: #e6edf3 !important;
        }
        
        /* Modern App Header View */
        .main-title {
            font-size: 2.3em;
            font-weight: 600;
            color: #f39c12;
            text-align: center;
            margin-top: 15px;
            letter-spacing: -0.5px;
        }
        .sub-title {
            color: #8b949e;
            font-size: 1.0em;
            text-align: center;
            margin-bottom: 25px;
        }
        
        /* Luxury Grid Cards Layout */
        .premium-card {
            background-color: #161a22;
            padding: 18px;
            border-radius: 14px;
            border: 1px solid #21262d;
            box-shadow: 0 8px 24px rgba(0,0,0,0.3);
            margin-bottom: 15px;
        }
        .pyramid-card {
            background-color: #1f242c;
            padding: 14px;
            border-radius: 10px;
            border-left: 5px solid #f39c12;
            margin-bottom: 12px;
        }
        .pyramid-label {
            font-size: 0.8em;
            text-transform: uppercase;
            color: #f39c12;
            font-weight: 600;
            margin-bottom: 4px;
            letter-spacing: 0.5px;
        }
        .pyramid-content {
            color: #f0f6fc;
            font-size: 1.0em;
        }
        .match-card {
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
            padding: 22px;
            border-radius: 12px;
            border: 2px solid #f39c12;
            box-shadow: 0 10px 30px rgba(243, 156, 18, 0.2);
            margin-top: 15px;
            text-align: center;
        }
        
        /* Formatting Streamlit Tabs for clean mobile scrolling viewports */
        div[data-testid="stTabBar"] {
            justify-content: center !important;
            background-color: transparent !important;
        }
        button[data-testid="stHeaderActionButton"] {
            display: none !important;
        }
        </style>
        
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
        <link rel="apple-touch-icon" href="https://images.unsplash.com/photo-1541643600914-78b084683601?w=500&q=80">
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='main-title'>⚗️ Perfume AI Analyzer</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Luxury Scent Vectors & Dynamic Pyramid Core</div>", unsafe_allow_html=True)
    
    df = load_verified_perfumes()
    
    # Minimalistic metric for clean mobile display view
    st.sidebar.markdown("### 📊 Engine Metadata")
    st.sidebar.metric("Verified Library Size", f"{len(df)} Bottles")
    st.sidebar.caption("Afeka College Project Presentation")
    
    tab1, tab2 = st.tabs(["🔍 Search Catalog", "🧪 Custom Scent Lab"])
    
    with tab1:
        search_query = st.text_input("Type bottle name (e.g., Versace Eros, Xerjoff Naxos):", "Xerjoff Naxos")
        if search_query:
            matched_df = df[df['name'].str.contains(search_query, case=False, na=False)]
            if not matched_df.empty:
                if len(matched_df) > 1:
                    selected_perfume = st.selectbox("Select exact match formulation:", matched_df['name'].tolist())
                    perfume_info = matched_df[matched_df['name'] == selected_perfume].iloc[0]
                else:
                    perfume_info = matched_df.iloc[0]
                
                profile = calculate_pyramid_profile(perfume_info['pyramid'])
                
                fig = px.pie(names=list(profile.keys()), values=list(profile.values()), hole=0.4, color_discrete_sequence=px.colors.sequential.Sunset_r)
                fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=10, b=10, l=10, r=10))
                st.plotly_chart(fig, use_container_width=True)
                
                parts = str(perfume_info['pyramid']).split('|')
                st.markdown(f"<div class='pyramid-card'><div class='pyramid-label'>🟢 Top Notes</div><div class='pyramid-content'>{format_note_text(parts[0])}</div></div>", unsafe_allow_html=True)
                st.markdown(f"<div class='pyramid-card'><div class='pyramid-label'>🟡 Heart Notes</div><div class='pyramid-content'>{format_note_text(parts[1] if len(parts)>1 else '')}</div></div>", unsafe_allow_html=True)
                st.markdown(f"<div class='pyramid-card'><div class='pyramid-label'>🔴 Base Notes</div><div class='pyramid-content'>{format_note_text(parts[2] if len(parts)>2 else '')}</div></div>", unsafe_allow_html=True)
                
                st.write("---")
                st.markdown("#### 🧠 Explainable AI Driver Vector Tags:")
                all_notes = str(perfume_info['pyramid']).replace('|', ' ').split()
                for category, keywords in NOTE_CATEGORIES.items():
                    matched = [note for note in all_notes if note in keywords]
                    if matched:
                        formatted_matches = format_note_text(" ".join(set(matched)))
                        st.success(f"**{category} Matrix** driven by: `{formatted_matches}`")
            else: st.error("❌ No matches found in database.")

    with tab2:
        st.markdown("### Build Your Custom Liquid Formula")
        
        formatted_options_map = {note: note.replace("_", " ").title() for note in ALL_UNIQUE_NOTES}
        reverse_map = {v: k for k, v in formatted_options_map.items()}
        
        top_sel = st.multiselect("🟢 Choose Top Notes (First Impression):", options=list(formatted_options_map.values()))
        mid_sel = st.multiselect("🟡 Choose Heart Notes (Core Scent Flow):", options=list(formatted_options_map.values()))
        base_sel = st.multiselect("🔴 Choose Base Notes (Dry Down Longevity):", options=list(formatted_options_map.values()))
            
        if top_sel or mid_sel or base_sel:
            custom_pyramid_str = f"{' '.join([reverse_map[n] for n in top_sel])} | {' '.join([reverse_map[n] for n in mid_sel])} | {' '.join([reverse_map[n] for n in base_sel])}"
            custom_profile = calculate_pyramid_profile(custom_pyramid_str)
            
            fig_custom = px.pie(names=list(custom_profile.keys()), values=list(custom_profile.values()), hole=0.4, color_discrete_sequence=px.colors.sequential.Sunset_r)
            fig_custom.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=10, b=10, l=10, r=10))
            st.plotly_chart(fig_custom, use_container_width=True)
            
            for label, val in custom_profile.items():
                st.metric(label=f"{label} Structural Mix Density", value=f"{val}%")
                
            best_match, match_score = find_closest_perfume_match(custom_profile, df)
            if best_match:
                st.markdown(f"<div class='match-card'><div style='color:#f39c12; font-weight:600; font-size:0.9em; letter-spacing:1px;'>🏆 AI DATABASE CLONE MATCH</div><div style='font-size:1.7em; color:white; font-weight:600; margin-top:5px;'>{best_match}</div><div style='color:#a3e635; margin-top:5px; font-weight:600;'>🎯 Similarity Index: {match_score}%</div></div>", unsafe_allow_html=True)
        else: st.info("💡 Select notes in the layers above to start the simulation.")

if __name__ == "__main__":
    main()