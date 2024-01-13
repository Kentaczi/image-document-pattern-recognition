import cv2
from augraphy import NoiseTexturize, Markup, Letterpress
import os

images = os.listdir('./original_pngs')
os.makedirs('./noise_texturize_pngs', exist_ok=True)
os.makedirs('./markup_pngs', exist_ok=True)
os.makedirs('./letterpress_pngs', exist_ok=True)

# augmentacja obrazów pod kątem szumu
for im_name in images:
    im_p = os.path.join('./original_pngs', im_name)
    original_image = cv2.imread(im_p, flags=cv2.COLOR_BGR2RGB)
    noise_texturize = NoiseTexturize(
        sigma_range=(3, 10),
        turbulence_range=(2, 5),
        texture_width_range=(100, 500),
        texture_height_range=(100, 500),
    )

    augmented_image = noise_texturize(original_image)

    cv2.imwrite(os.path.join('./noise_texturize_pngs', im_name), augmented_image)

# augmentacja obrazów pod kątem nakładania losowych linii
for im_name in images:
    im_p = os.path.join('./original_pngs', im_name)
    original_image = cv2.imread(im_p, flags=cv2.COLOR_BGR2RGB)
    markup = Markup(
        num_lines_range=(6, 25),
        markup_length_range=(0.5, 1),
        markup_thickness_range=(1, 7),
        markup_type='random',
        markup_ink='random',
        markup_color=(0, 0, 0),
        large_word_mode='random',
        single_word_mode=False,
        repetitions=1
    )

    augmented_image = markup(original_image)

    cv2.imwrite(os.path.join('./markup_pngs', im_name), augmented_image)

# augmentacja obrazów pod kątem blura
for im_name in images:
    im_p = os.path.join('./original_pngs', im_name)
    original_image = cv2.imread(im_p, flags=cv2.COLOR_BGR2RGB)
    letterpress = Letterpress(n_samples=(200, 500),
                              n_clusters=(300, 800),
                              std_range=(1500, 5000),
                              value_range=(200, 255),
                              value_threshold_range=(64, 256),
                              blur=1
                              )

    augmented_image = letterpress(original_image)

    cv2.imwrite(os.path.join('./letterpress_pngs', im_name), augmented_image)
