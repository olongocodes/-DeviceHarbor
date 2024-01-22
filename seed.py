from main import app
from models import db, Product

categories = [
    "Tablets",
    "Smartwatches",
    "Headphones and earphones",
    "Cameras and accessories",
    "Smart home devices (smart speakers, thermostats, etc.)",
    "Desktop computers",
    "Computer monitors",
    "Keyboards and mice",
    "Printers and scanners",
    "External hard drives"
]

exchange_rate = 158.97
products = [
    # Tablets
    {"name": "iPad Pro", "quantity": 20, "category": categories[0], "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRL9sMpTMN2ew2IB9oyXFoTiZ5IbmGo8bKT1-MLZzi8Ug&s", "price": 799.99},
    {"name": "Samsung Galaxy Tab S7", "quantity": 15, "category": categories[0], "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBwk2JKV1jqEjbEGD6UaRtlfbUFtAOWX-q2SZU7JevZJ0yC4KhFL93CDLRDw&s", "price": 649.99},
    # Smartwatches
    {"name": "Apple Watch Series 6", "quantity": 25, "category": categories[1], "image_url": "https://www.bing.com/images/create/garmin-venu-2/1-65ad36758d244e59b32c4940325daac2?id=%2fIimnfdmgoqCgw3e8yZB5w%3d%3d&view=detailv2&idpp=genimg&noidpclose=1&FORM=SYDBIC", "price": 399.99},
    {"name": "Garmin Venu 2", "quantity": 18, "category": categories[1], "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwLNd52kgovJcK1KLvo1O4BNdA69O66dGXHjPzJq9aEaRqQr6GVJ78xXE3Mg&s", "price": 349.99},
    # Headphones and earphones
    {"name": "Sony WH-1000XM4", "quantity": 30, "category": categories[2], "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsScY12OOp2jZL3EZRtUPbTZtapCu_FTXdtTMeK50EIeSKD3wwbuqywsZK_g&s", "price": 349.99},
    {"name": "AirPods Pro", "quantity": 22, "category": categories[2], "image_url": "https://www.tomsguide.com/opinion/sonys-wh-1000xm4-headphones-are-great-heres-how-i-made-them-sound-even-better", "price": 249.99},
    # Cameras and accessories
    {"name": "Canon EOS R5", "quantity": 12, "category": categories[3], "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbQs82MLSc6GJ6PSqgT2S4ZHRwDDCk5P-VpTvEbqTDd0zE0lCIUVOnY6SoUQ&s", "price": 379.99},
    {"name": "DJI Mavic Air 2", "quantity": 15, "category": categories[3], "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRamGqTcLmvviYMXbQbur3CSB9FguDqm9YhcU7_bboadum4P3pMljtmJdI4Lw&s", "price": 799.99},
    # Smart home devices
    {"name": "Amazon Echo Dot", "quantity": 28, "category": categories[4], "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIQapF7irIoXUmUo_iVIGbWzSHBQjAyla81FqYuGdeXOsXo0HWBNfQx3Lgpg&s", "price": 49.99},
    {"name": "Nest Learning Thermostat", "quantity": 10, "category": categories[4], "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWaKqgiJtvAnXR8sRmxYSH2nkGKDPW3-cCSpxEXsNrLsB9rIwbr3tpu6ACwA&s", "price": 249.99},
    # Desktop computers
    {"name": "Alienware Aurora R10", "quantity": 8, "category": categories[5], "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRN_rd1WYmIrFhpR44rlD4gt9K8a3RrLk1VAALEm_VcKKaOo_pTDu-FqHJpcw&s", "price": 1599.99},
    {"name": "HP Pavilion Gaming Desktop", "quantity": 15, "category": categories[5], "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzm78VDLF0rAighbJaD7ywhItFsYm-xa7tZlfRoEMS-1Gj6b66hqzTGwM0Dw&s", "price": 849.99},
    # Computer monitors
    {"name": "LG UltraGear 27GN950-B", "quantity": 20, "category": categories[6], "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTfBWrcsmVwOBE-75r3POqTAl-jG6j7k1GZvSf4FFDEbQ&s", "price": 699.99},
    {"name": "Dell S2419HGF", "quantity": 18, "category": categories[6], "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRytZkN_5ejash9Nqq6SCBBNXEpZNoRExTtb6KGK2LZc7vDSkuDl4j19da2CLeX2NhL5oI&usqp=CAU", "price": 179.99},
    # Keyboards and mice
    {"name": "Logitech G Pro X Mechanical Gaming Keyboard", "quantity": 25, "category": categories[7], "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQd7955qLRYH1jgMJwP9hCrBtu1Pzdk2sbnRq9wrSlMGxL3CDaGlgbpLxW0eg&s", "price": 149.99},
    {"name": "Razer DeathAdder Elite Gaming Mouse", "quantity": 30, "category": categories[7], "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzrJb_ff2snmYJwQ3BJhVNv4BD0S0EtImM6kVaDM7lAA&s", "price": 69.99},
    # Printers and scanners
    {"name": "HP LaserJet Pro M404dn", "quantity": 12, "category": categories[8], "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQn6lWpVB_1kv1qI3orkCjg17H6iNO7iafZ5cHmjB8tZDO4sE2hhDmRKBuwWw&s", "price": 24999},
    {"name": "Epson WorkForce ES-400", "quantity": 15, "category": categories[8], "image_url": "", "price": 32999},
    # External hard drives
    {"name": "Samsung T5 Portable SSD", "quantity": 20, "category": categories[9], "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTp5A7shP85pyvAwWdkKWRVbqAKNHcMuM4O1ibC4XuAe2TLl3eC0vZmWiFlYg&s", "price": 14999},
    {"name": "Seagate Backup Plus Hub", "quantity": 18, "category": categories[9], "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQs-Yuanv0vbLGsoKt43WCm5PvQdM6rTjgKXw&usqp=CAU", "price": 10999},

    # Tablets
    {"name": "Lenovo mouse series 5", "quantity": 20, "category": categories[0], "image_url": "https://cdn.cs.1worldsync.com/f2/7d/f27d99e3-6495-4324-95de-b4e896758643.jpg", "price": 799.99},
    {"name": "usb Koot 64gb", "quantity": 15, "category": categories[1], "image_url": "https://m.media-amazon.com/images/I/51o2VzSkYJL.AC_UF894,1000_QL80.jpg", "price": 649.99},
    # hp and camera
    {"name": "Hp pavillion Series 6", "quantity": 25, "category": categories[2], "image_url": "https://p2-ofp.static.pub/fes/cms/2022/08/01/ycumf4z4oia108az0pq0kzvf17wdws486228.png", "price": 399.99},
    {"name": "Nixon camera original series", "quantity": 18, "category": categories[4], "image_url": "https://i.pinimg.com/originals/56/af/ea/56afea1c009e67eae14c0de360a78a05.png", "price": 349.99},
    # smart devices
    {"name": "Dell ", "quantity": 30, "category": categories[2], "image_url": "https://i.dell.com/is/image/DellContent/content/dam/ss2/product-images/page/category/laptop/category-page-mod-xps-13-9320-sl-right-800x620.png?fmt=png-alpha&wid=800&hei=620", "price": 349.99},
    {"name": "Iphone 14 pro max 1 tb", "quantity": 22, "category": categories[5], "image_url": "https://www.apple.com/newsroom/images/product/iphone/standard/Apple_iPhone-13-Pro_iPhone-13-Pro-Max_09142021_inline.jpg.large.jpg", "price": 1249.99},
    # Cameras and accessories
    {"name": "smart wtch EOS R5", "quantity": 12, "category": categories[3], "image_url": "https://www.leafstudios.in/cdn/shop/products/Main_6bd752ac-4c5f-44a5-926d-bb26a1335819_grande.jpg?v=1671601899", "price": 379.99},
    {"name": "Canon Air 2", "quantity": 15, "category": categories[4], "image_url": "https://m.media-amazon.com/images/I/71-8KPWyu0L.AC_UF894,1000_QL80.jpg", "price": 799.99},
    # computers
    {"name": "Hp-elitebook 840-G5", "quantity": 28, "category": categories[7], "image_url": "https://cdn.ttgtmedia.com/rms/onlineimages/hp_elitebook_mobile.jpg", "price": 49.99},
    {"name": "Hp-elitebook 840-G4 series 2", "quantity": 10, "category": categories[5], "image_url": "https://cdn.ttgtmedia.com/rms/onlineimages/hp_elitebook_mobile.jpg", "price": 249.99},
]


# Convert prices to KSH using the exchange rate
for product in products:
    product['price'] = int(product['price'] * exchange_rate)
with app.app_context():
    db.session.add_all([Product(**product) for product in products])
    db.session.commit()