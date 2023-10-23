from numpy import ones, uint8, flip
from pygame.surfarray import pixels_alpha
from pygame.transform import smoothscale


def generate_round_corner_mask(radius, curvature):
    arr = ones((radius, radius), dtype=uint8)*255
    for i in range(radius):
        for j in range(radius):
            if (radius-i)**curvature + (radius-j)**curvature >= radius**curvature:
                arr[i, j] = 0
    return arr


def add_corners(surface, radius=20, curvature=3, corners={1, 2, 3, 4}):
    factor = 4
    size = surface.get_size()
    scaled_radius = radius * factor
    scaled_size = size[0]*factor, size[1]*factor
    scaled_surface = smoothscale(surface, scaled_size)

    alpha_arr = pixels_alpha(scaled_surface)
    mask = generate_round_corner_mask(radius*factor, curvature)

    if 1 in corners:
        alpha_arr[:scaled_radius, :scaled_radius] = mask
    if 2 in corners:
        alpha_arr[-scaled_radius:, :scaled_radius] = flip(mask, axis=0)
    if 3 in corners:
        alpha_arr[:scaled_radius, -scaled_radius:] = flip(mask, axis=1)
    if 4 in corners:
        alpha_arr[-scaled_radius:, -scaled_radius:] = flip(flip(mask, axis=1), axis=0)

    return smoothscale(scaled_surface, size)