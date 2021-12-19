from PIL import Image

santa = Image.open('data/pt6/santa_tonakai_sori.png')

santa_45 = santa.rotate(45, fillcolor=(255, 0, 0), expand=True)
santa_45.save('data/pt6/santa_tonakai_sori_rotate45.png')

yoroshiku = Image.open('data/pt6/message_yoroshiku.png')
hologram = Image.open('data/pt6/hologram_kira_sticker_color.png').resize(yoroshiku.size)

yoroshiku_mask = yoroshiku.convert('L')
yoroshiku_mask = yoroshiku_mask.point(lambda i: 255 if i != 255 else 0)

background = Image.new('RGB', yoroshiku.size)

synthesized = Image.composite(background, hologram, yoroshiku_mask)

synthesized.save('data/pt6/synthesized.png')