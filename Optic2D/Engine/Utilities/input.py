import pygame

class InputHandler:
    def __init__(self):
        self.keys = {}
        self.key_mapping = {
            "left": pygame.K_LEFT,
            "right": pygame.K_RIGHT,
            "up": pygame.K_UP,
            "down": pygame.K_DOWN,
            "a": pygame.K_a,
            "b": pygame.K_b,
            "c": pygame.K_c,
            "d": pygame.K_d,
            "e": pygame.K_e,
            "f": pygame.K_f,
            "g": pygame.K_g,
            "h": pygame.K_h,
            "i": pygame.K_i,
            "j": pygame.K_j,
            "k": pygame.K_k,
            "l": pygame.K_l,
            "m": pygame.K_m,
            "n": pygame.K_n,
            "o": pygame.K_o,
            "p": pygame.K_p,
            "q": pygame.K_q,
            "r": pygame.K_r,
            "s": pygame.K_s,
            "t": pygame.K_t,
            "u": pygame.K_u,
            "v": pygame.K_v,
            "w": pygame.K_w,
            "x": pygame.K_x,
            "y": pygame.K_y,
            "z": pygame.K_z,
            "0": pygame.K_0,
            "1": pygame.K_1,
            "2": pygame.K_2,
            "3": pygame.K_3,
            "4": pygame.K_4,
            "5": pygame.K_5,
            "6": pygame.K_6,
            "7": pygame.K_7,
            "8": pygame.K_8,
            "9": pygame.K_9,
            "space": pygame.K_SPACE,
            "enter": pygame.K_RETURN,
            "esc": pygame.K_ESCAPE,
            # Add more keys as needed
        }

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                self.keys[event.key] = True

            elif event.type == pygame.KEYUP:
                self.keys[event.key] = False

    def is_key_pressed(self, key_name):
        key = self.key_mapping.get(key_name)
        if key is not None:
            return self.keys.get(key, False)
        else:
            print(f"Warning: Unknown key name '{key_name}'")
            return False
