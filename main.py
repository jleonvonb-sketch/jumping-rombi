import pygame
import sys
import os
import random
import math
import json

# --- Configuración Base ---
WIDTH, HEIGHT = 800, 600
FPS = 60
TILE_SIZE = 32

COLOR_BG = (15, 15, 25)
TEXTURES = {}

def init_textures():
    def make_tex(draw_func, size=(TILE_SIZE, TILE_SIZE)):
        surf = pygame.Surface(size, pygame.SRCALPHA)
        draw_func(surf)
        return surf
        
    def t_wall(s):
        pygame.draw.rect(s, (80, 80, 100), (0, 0, 32, 32))
        pygame.draw.rect(s, (60, 60, 80), (2, 2, 28, 28))
    def t_player(s): pygame.draw.rect(s, (0, 180, 255), (6, 4, 20, 28))
    def t_coin(s):
        pygame.draw.circle(s, (255, 215, 0), (16, 16), 10)
        pygame.draw.circle(s, (255, 255, 150), (16, 16), 6)
    def t_key(s):
        pygame.draw.rect(s, (0, 255, 150), (8, 12, 16, 8))
        pygame.draw.circle(s, (0, 255, 150), (10, 16), 6)
    def t_spike(s):
        pygame.draw.polygon(s, (200, 50, 50), [(16, 10), (4, 32), (28, 32)])
        pygame.draw.polygon(s, (255, 100, 100), [(16, 16), (10, 32), (22, 32)])
    def t_door(s):
        pygame.draw.rect(s, (150, 50, 50), (4, 0, 24, 32))
        pygame.draw.circle(s, (255, 200, 0), (22, 16), 3)
    def t_enemy(s):
        pygame.draw.rect(s, (255, 0, 100), (4, 8, 24, 24))
        pygame.draw.circle(s, (255, 255, 255), (10, 14), 3)
        pygame.draw.circle(s, (255, 255, 255), (22, 14), 3)
    def t_boss(s): 
        pygame.draw.rect(s, (150, 0, 255), (0, 0, 64, 64))
        pygame.draw.circle(s, (255, 0, 0), (20, 20), 8)
        pygame.draw.circle(s, (255, 0, 0), (44, 20), 8)
    def t_trampoline(s):
        pygame.draw.rect(s, (50, 150, 255), (4, 20, 24, 12))
        pygame.draw.rect(s, (200, 255, 255), (4, 20, 24, 4))
        
    # Combate
    def t_bullet(s): pygame.draw.circle(s, (255, 255, 0), (16, 16), 4)
    def t_rocket(s): pygame.draw.rect(s, (200, 100, 50), (12, 14, 12, 6))
    def t_explosion(s): pygame.draw.circle(s, (255, 100, 0, 180), (48, 48), 48)
        
    # UI y Nuevos Items
    def t_heart(s):
        pygame.draw.circle(s, (255, 50, 50), (10, 10), 8)
        pygame.draw.circle(s, (255, 50, 50), (22, 10), 8)
        pygame.draw.polygon(s, (255, 50, 50), [(2, 12), (30, 12), (16, 28)])
    def t_heart_empty(s):
        pygame.draw.circle(s, (100, 30, 30), (10, 10), 8, 2)
        pygame.draw.circle(s, (100, 30, 30), (22, 10), 8, 2)
        pygame.draw.polygon(s, (100, 30, 30), [(2, 12), (30, 12), (16, 28)], 2)
    
    # Armas UI
    def t_gun(s):
        pygame.draw.rect(s, (150, 150, 150), (6, 14, 20, 6))
        pygame.draw.rect(s, (80, 80, 80), (6, 20, 6, 8))
    def t_rifle(s):
        pygame.draw.rect(s, (100, 150, 100), (2, 14, 28, 6))
        pygame.draw.rect(s, (50, 50, 50), (20, 20, 6, 8))
        pygame.draw.rect(s, (50, 50, 50), (6, 20, 6, 8))
    def t_rpg(s):
        pygame.draw.rect(s, (50, 100, 50), (0, 12, 32, 10))
        pygame.draw.rect(s, (200, 100, 0), (28, 10, 4, 14))
        pygame.draw.rect(s, (30, 30, 30), (14, 22, 6, 8))

    def t_magnet(s):
        pygame.draw.arc(s, (200, 50, 50), (4, 4, 24, 24), 0, 3.14, 6)
        pygame.draw.rect(s, (200, 200, 200), (4, 16, 6, 6))
        pygame.draw.rect(s, (200, 200, 200), (22, 16, 6, 6))
    def t_potion(s):
        pygame.draw.polygon(s, (200, 200, 200), [(12, 4), (20, 4), (16, 12)])
        pygame.draw.circle(s, (255, 50, 150), (16, 20), 10)
    def t_boots(s):
        pygame.draw.rect(s, (139, 69, 19), (8, 12, 10, 16))
        pygame.draw.rect(s, (139, 69, 19), (8, 24, 16, 6))
        pygame.draw.rect(s, (255, 255, 0), (10, 18, 12, 4))
    def t_shield(s):
        pygame.draw.polygon(s, (50, 150, 255), [(16, 2), (4, 8), (4, 20), (16, 30), (28, 20), (28, 8)])
        pygame.draw.polygon(s, (200, 255, 255), [(16, 6), (8, 10), (8, 18), (16, 26), (24, 18), (24, 10)])
    def t_spring(s):
        pygame.draw.rect(s, (150, 150, 150), (8, 24, 16, 6))
        pygame.draw.line(s, (200, 200, 200), (10, 24), (22, 16), 3)
        pygame.draw.line(s, (200, 200, 200), (10, 16), (22, 8), 3)
    def t_double_coin(s):
        pygame.draw.circle(s, (200, 150, 0), (12, 12), 10)
        pygame.draw.circle(s, (255, 215, 0), (20, 20), 10)

    TEXTURES.update({"wall": make_tex(t_wall), "player": make_tex(t_player), "coin": make_tex(t_coin),
                     "key": make_tex(t_key), "spike": make_tex(t_spike), "door": make_tex(t_door),
                     "enemy": make_tex(t_enemy), "boss": make_tex(t_boss, (64, 64)), "trampoline": make_tex(t_trampoline),
                     "bullet": make_tex(t_bullet), "rocket": make_tex(t_rocket), "explosion": make_tex(t_explosion, (96, 96)),
                     "heart": make_tex(t_heart), "heart_empty": make_tex(t_heart_empty), "gun": make_tex(t_gun),
                     "rifle": make_tex(t_rifle), "rpg": make_tex(t_rpg), "magnet": make_tex(t_magnet),
                     "potion": make_tex(t_potion), "boots": make_tex(t_boots), "shield": make_tex(t_shield),
                     "spring": make_tex(t_spring), "double_coin": make_tex(t_double_coin)})

# --- SISTEMA DE GUARDADO (JSON) ---
def get_save_dir():
    home = os.path.expanduser("~")
    base = "/userdata/system" if os.path.exists("/userdata") else home
    save_dir = os.path.join(base, "superplataformas")
    if not os.path.exists(save_dir): os.makedirs(save_dir, exist_ok=True)
    return save_dir

SAVE_DIR = get_save_dir()
SAVE_FILE = os.path.join(SAVE_DIR, "savegame_v6.json")

def save_data(player_data, map_data):
    try:
        with open(SAVE_FILE, "w") as f:
            json.dump({"player": player_data, "map": map_data}, f)
    except: pass

def load_data():
    default_player = {"hp": 5, "max_hp": 5, "max_jumps": 2, "coins": 0, "keys": 0, "weapon": "gun", 
                      "owns_gun": True, "owns_rifle": False, "owns_rpg": False,
                      "has_magnet": False, "has_speed": False, "has_shield": False, "double_coin": False}
    default_map = {"current_node": 1, "max_level_reached": 1}
    
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r") as f:
                data = json.load(f)
                return data.get("player", default_player), data.get("map", default_map)
        except: pass
    return default_player, default_map

def delete_all_data():
    if os.path.exists(SAVE_FILE): os.remove(SAVE_FILE)

# --- ITEMS DE LA TIENDA MEJORADA ---
SHOP_ITEMS = [
    {"id": "heal", "name": "Curar (+1 HP)", "desc": "Recupera 1 punto de vida.", "cost": 5, "tex": "heart"},
    {"id": "full_heal", "name": "Poción Máxima", "desc": "Recupera toda tu vida.", "cost": 15, "tex": "potion"},
    {"id": "max_hp", "name": "Vida Máxima", "desc": "Agrega un corazón extra.", "cost": 30, "tex": "heart"},
    {"id": "magnet", "name": "Imán", "desc": "Atrae las monedas cercanas.", "cost": 40, "tex": "magnet"},
    {"id": "speed_boots", "name": "Botas Rápidas", "desc": "Aumenta tu velocidad.", "cost": 50, "tex": "boots"},
    {"id": "extra_jump", "name": "Salto Triple", "desc": "3 saltos en el aire.", "cost": 60, "tex": "spring"},
    {"id": "shield", "name": "Escudo de Energía", "desc": "Absorbe el próximo golpe.", "cost": 60, "tex": "shield"},
    {"id": "double_coin", "name": "Monedas x2", "desc": "Las monedas valen doble.", "cost": 100, "tex": "double_coin"},
    {"id": "gun", "name": "Pistola", "desc": "Equipar Pistola.", "cost": 0, "tex": "gun"},
    {"id": "rifle", "name": "Rifle Asalto", "desc": "Disparo rápido.", "cost": 80, "tex": "rifle"},
    {"id": "rpg", "name": "Lanzacohetes", "desc": "Explosiones masivas.", "cost": 150, "tex": "rpg"},
    {"id": "back", "name": "Volver", "desc": "Salir de la tienda.", "cost": 0, "tex": "door"}
]

# --- CLASES ---
class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width; self.height = height

    def apply(self, entity): return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = min(0, max(-(self.width - WIDTH), -target.rect.centerx + WIDTH // 2))
        y = min(0, max(-(self.height - HEIGHT), -target.rect.centery + HEIGHT // 2))
        self.camera.topleft = (x, y)

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, target_x, target_y, p_type="bullet"):
        super().__init__()
        self.type = p_type
        self.image = TEXTURES["rocket"] if p_type == "rpg" else TEXTURES["bullet"]
        self.rect = self.image.get_rect(center=(x, y))
        
        angle = math.atan2(target_y - y, target_x - x)
        speed = 15 if p_type == "rifle" else (8 if p_type == "rpg" else 10)
        
        self.dx = math.cos(angle) * speed
        self.dy = math.sin(angle) * speed
        self.damage = 5 if p_type == "rpg" else (1 if p_type == "rifle" else 2)

    def update(self, walls):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if pygame.sprite.spritecollideany(self, walls) or self.rect.y > 2000:
            self.kill()
            return True
        return False

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = TEXTURES["explosion"]
        self.rect = self.image.get_rect(center=(x, y))
        self.timer = 15

    def update(self, walls):
        self.timer -= 1
        if self.timer <= 0: self.kill()

class StaticObject(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        super().__init__()
        self.image = TEXTURES[type]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.hitbox = pygame.Rect(x + 10, y + 24, 12, 8) if type == "spike" else self.rect

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, level):
        super().__init__()
        self.image = TEXTURES["enemy"]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.direction = 1
        self.speed = 2 + (level // 10)
        self.hp = 3 + (level // 5)

    def update(self, walls):
        self.rect.x += self.speed * self.direction
        if pygame.sprite.spritecollideany(self, walls):
            self.direction *= -1

class Boss(pygame.sprite.Sprite):
    def __init__(self, x, y, level):
        super().__init__()
        self.image = TEXTURES["boss"]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.max_hp = 40 + (level * 3)
        self.hp = self.max_hp
        self.speed = 3
        self.vel_y = 0
        self.jump_timer = 0

    def update(self, walls, player):
        if self.rect.centerx < player.rect.centerx: self.rect.x += self.speed
        elif self.rect.centerx > player.rect.centerx: self.rect.x -= self.speed
        
        self.vel_y += 0.5
        self.rect.y += self.vel_y
        on_ground = False
        for w in walls:
            if self.rect.colliderect(w.rect):
                if self.vel_y > 0: self.rect.bottom = w.rect.top; self.vel_y = 0; on_ground = True
        
        self.jump_timer += 1
        if on_ground and self.jump_timer > 80 and random.random() < 0.15:
            self.vel_y = -13
            self.jump_timer = 0

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = TEXTURES["player"]
        self.rect = self.image.get_rect()
        self.vel = pygame.Vector2(0, 0)
        
        self.facing = 1
        self.jumps = 0; self.jump_was_pressed = False
        self.cooldown = 0
        
        self.joystick = pygame.joystick.Joystick(0) if pygame.joystick.get_count() > 0 else None
        if self.joystick: self.joystick.init()
        
        self.inv = {} # Se llenará con load_data

    def update(self, walls):
        move = 0; jump_now = False
        keys = pygame.key.get_pressed()
        move = (keys[pygame.K_RIGHT] or keys[pygame.K_d]) - (keys[pygame.K_LEFT] or keys[pygame.K_a])
        jump_now = keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]

        if self.joystick:
            if self.joystick.get_axis(0) > 0.3: move = 1
            elif self.joystick.get_axis(0) < -0.3: move = -1
            if self.joystick.get_button(0): jump_now = True

        speed_mult = 7 if self.inv.get("has_speed") else 5
        self.vel.x = move * speed_mult
        if move != 0: self.facing = 1 if move > 0 else -1

        self.vel.y = min(self.vel.y + 0.8, 15)

        self.rect.x += int(self.vel.x)
        on_wall_left = on_wall_right = False
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if self.vel.x > 0: self.rect.right = wall.rect.left; on_wall_right = True
                elif self.vel.x < 0: self.rect.left = wall.rect.right; on_wall_left = True

        self.rect.y += int(self.vel.y)
        on_ground = False
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if self.vel.y > 0: self.rect.bottom = wall.rect.top; self.vel.y = 0; on_ground = True
                elif self.vel.y < 0: self.rect.top = wall.rect.bottom; self.vel.y = 0

        if (on_wall_left or on_wall_right) and not on_ground and self.vel.y > 0: self.vel.y = 2 
        if on_ground: self.jumps = 0 

        if jump_now and not self.jump_was_pressed:
            if on_ground:
                self.vel.y = -12; self.jumps = 1
            elif on_wall_left or on_wall_right: # Wall jump infinito
                self.vel.y = -12; self.jumps = 0 
            elif self.jumps < self.inv["max_jumps"]:
                self.vel.y = -11; self.jumps += 1
        self.jump_was_pressed = jump_now
        
        if self.cooldown > 0: self.cooldown -= 1

# --- GAME ---
class Game:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Super Plataformas Boss Edition")

        self.font = pygame.font.SysFont(None, 36)
        self.title_font = pygame.font.SysFont(None, 64)
        self.ui_font = pygame.font.SysFont(None, 24)

        init_textures()
        
        self.state = "MAP"
        self.menu_options = []
        self.menu_selected = 0
        self.clock = pygame.time.Clock()

        self.player = Player()
        p_data, m_data = load_data()
        self.player.inv = p_data
        
        self.map_data = m_data
        self.map_scroll_x = 0

    def save_game(self): save_data(self.player.inv, self.map_data)

    def get_map_node_pos(self, lvl):
        # Generación determinista del mapa ondulado (Tryhard no-soso)
        x = 100 + (lvl - 1) * 160
        y = HEIGHT // 2 + math.sin(lvl * 1.2) * 150
        return (int(x), int(y))

    def generate_level(self, n):
        width, height = 30 + (n * 3), 15
        level_map = [[" " for _ in range(width)] for _ in range(height)]
        for x in range(width): level_map[0][x] = "W"; level_map[height-1][x] = "W"
        for y in range(height): level_map[y][0] = "W"; level_map[y][width-1] = "W"
        
        highest_y = height
        key_pos = (width - 4, height - 3) # Posición por defecto por si acaso

        for _ in range(10 + n * 2):
            pw, px, py = random.randint(3, 7), random.randint(2, width - 9), random.randint(4, height - 3)
            
            # Guardamos la posición de la plataforma más alta que se genere
            if py < highest_y:
                highest_y = py
                key_pos = (px + pw // 2, py - 1) # Justo en medio de esa plataforma

            for i in range(pw):
                level_map[py][px+i] = "W"
                if random.random() < 0.25 and level_map[py-1][px+i] == " ":
                    level_map[py-1][px+i] = random.choice(["C", "C", "S", "E", "T"])
                    
        level_map[height-2][2] = "P" # Jugador (Abajo a la izquierda)
        level_map[height-2][width-3] = "D" # Puerta (Abajo a la derecha)
        
        # 1. Colocamos la llave en la zona más alta encontrada
        kx, ky = key_pos
        level_map[ky][kx] = "K"
        
        # 2. Modo Tryhard: Protegemos la llave con pinchos a los lados
        if level_map[ky][kx-1] in [" ", "C"]: level_map[ky][kx-1] = "S "
        if level_map[ky][kx+1] in [" ", "C"]: level_map[ky][kx+1] = " S"

        return level_map

    def generate_boss_level(self):
        width, height = 30, 15
        level_map = [[" " for _ in range(width)] for _ in range(height)]
        for x in range(width): level_map[0][x] = "W"; level_map[height-1][x] = "W"
        for y in range(height): level_map[y][0] = "W"; level_map[y][width-1] = "W"
        
        # Plataformas en la arena
        for i in range(5): level_map[height-5][4+i] = "W"; level_map[height-5][width-9+i] = "W"
        level_map[height-2][2] = "P"; level_map[height-4][width-5] = "B"
        return level_map

    def load_level(self, n):
        random.seed(n) # Niveles consistentes
        is_boss = (n % 10 == 0)
        layout = self.generate_boss_level() if is_boss else self.generate_level(n)

        self.camera = Camera(len(layout[0]) * TILE_SIZE, len(layout) * TILE_SIZE)
        self.walls, self.doors, self.enemies, self.bosses = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()
        self.coins, self.spikes, self.keys, self.trampolines = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()
        self.projectiles, self.explosions, self.all_sprites = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()

        for r, row in enumerate(layout):
            for c, cell in enumerate(row):
                x, y = c*TILE_SIZE, r*TILE_SIZE
                if cell == "W": obj = StaticObject(x, y, "wall"); self.walls.add(obj); self.all_sprites.add(obj)
                elif cell == "D" and not is_boss: obj = StaticObject(x, y, "door"); self.doors.add(obj); self.all_sprites.add(obj)
                elif cell == "C": obj = StaticObject(x, y, "coin"); self.coins.add(obj); self.all_sprites.add(obj)
                elif cell == "K": obj = StaticObject(x, y, "key"); self.keys.add(obj); self.all_sprites.add(obj)
                elif cell == "S": obj = StaticObject(x, y, "spike"); self.spikes.add(obj); self.all_sprites.add(obj)
                elif cell == "E": enemy = Enemy(x, y, n); self.enemies.add(enemy); self.all_sprites.add(enemy)
                elif cell == "T": obj = StaticObject(x, y, "trampoline"); self.trampolines.add(obj); self.all_sprites.add(obj)
                elif cell == "B": boss = Boss(x, y, n); self.bosses.add(boss); self.all_sprites.add(boss)
                elif cell == "P": self.player.rect.topleft = (x, y); self.player.vel = pygame.Vector2(0,0)

    def shoot(self, mouse_pos):
        if self.player.cooldown > 0: return
        world_x, world_y = mouse_pos[0] - self.camera.camera.x, mouse_pos[1] - self.camera.camera.y
        
        wpn = self.player.inv["weapon"]
        proj = Projectile(self.player.rect.centerx, self.player.rect.centery, world_x, world_y, wpn)
        self.projectiles.add(proj); self.all_sprites.add(proj)
        
        if wpn == "rifle": self.player.cooldown = 6
        elif wpn == "gun": self.player.cooldown = 15
        elif wpn == "rpg": self.player.cooldown = 45

    def take_damage(self):
        if self.player.inv.get("has_shield"):
            self.player.inv["has_shield"] = False
            self.player.vel.y = -10
            self.player.vel.x = -self.player.facing * 5
            return

        self.player.inv["hp"] -= 1
        if self.player.inv["hp"] > 0:
            self.load_level(self.map_data["current_node"]) # Reiniciar nivel
        else:
            # Muerte total: Volver al mapa
            self.player.inv["hp"] = self.player.inv["max_hp"]
            self.state = "MAP"

    def handle_menu_input(self, move, select, cancel):
        if move != 0: 
            if self.state == "SHOP":
                new_sel = self.menu_selected + move
                if 0 <= new_sel < len(self.menu_options): self.menu_selected = new_sel
            else:
                self.menu_selected = (self.menu_selected + move) % len(self.menu_options)
        
        if cancel:
            if self.state in ["PAUSED", "SHOP"]: self.state = "PLAYING"
            elif self.state == "CONFIRM_DELETE": self.state = "PAUSED"; self.menu_selected = 2

        if select:
            if self.state == "PAUSED":
                if self.menu_selected == 0: self.state = "PLAYING"
                elif self.menu_selected == 1: self.state = "SHOP"; self.menu_selected = 0; self.menu_options = SHOP_ITEMS
                elif self.menu_selected == 2: self.state = "MAP" # Salir al mapa
                elif self.menu_selected == 3: self.state = "CONFIRM_DELETE"; self.menu_selected = 0

            elif self.state == "CONFIRM_DELETE":
                if self.menu_selected == 0: self.state = "PAUSED"; self.menu_selected = 3
                elif self.menu_selected == 1: 
                    delete_all_data()
                    self.player.inv, self.map_data = load_data()
                    self.state = "MAP"

            elif self.state == "SHOP":
                item = SHOP_ITEMS[self.menu_selected]
                if item["id"] == "back":
                    self.state = "PAUSED"; self.menu_selected = 1
                else:
                    inv = self.player.inv
                    # Lógica de Armas
                    if item["id"] in ["gun", "rifle", "rpg"]:
                        own_key = f"owns_{item['id']}"
                        if inv.get(own_key):
                            inv["weapon"] = item["id"] # Equipar si ya la tiene
                        elif inv["coins"] >= item["cost"]:
                            inv["coins"] -= item["cost"]
                            inv[own_key] = True
                            inv["weapon"] = item["id"]
                    # Lógica de Mejoras
                    else:
                        if inv["coins"] >= item["cost"]:
                            if item["id"] == "heal" and inv["hp"] >= inv["max_hp"]: return
                            if item["id"] == "full_heal" and inv["hp"] >= inv["max_hp"]: return
                            if item["id"] == "magnet" and inv["has_magnet"]: return
                            if item["id"] == "speed_boots" and inv["has_speed"]: return
                            if item["id"] == "extra_jump" and inv["max_jumps"] >= 3: return
                            if item["id"] == "shield" and inv["has_shield"]: return
                            if item["id"] == "double_coin" and inv["double_coin"]: return

                            inv["coins"] -= item["cost"]
                            if item["id"] == "heal": inv["hp"] += 1
                            elif item["id"] == "full_heal": inv["hp"] = inv["max_hp"]
                            elif item["id"] == "max_hp": inv["max_hp"] += 1; inv["hp"] += 1
                            elif item["id"] == "magnet": inv["has_magnet"] = True
                            elif item["id"] == "speed_boots": inv["has_speed"] = True
                            elif item["id"] == "extra_jump": inv["max_jumps"] = 3
                            elif item["id"] == "shield": inv["has_shield"] = True
                            elif item["id"] == "double_coin": inv["double_coin"] = True
                    self.save_game()

    def draw_map(self):
        # 1. Fondo Parallax Cuadrícula
        self.screen.fill((15, 20, 35))
        target_cam_x = WIDTH//2 - self.get_map_node_pos(self.map_data["current_node"])[0]
        self.map_scroll_x += (target_cam_x - self.map_scroll_x) * 0.1 # Suavizado de cámara
        
        offset = self.map_scroll_x % 50
        for x in range(0, WIDTH + 50, 50): pygame.draw.line(self.screen, (30, 40, 60), (x + offset - 50, 0), (x + offset - 50, HEIGHT))
        for y in range(0, HEIGHT, 50): pygame.draw.line(self.screen, (30, 40, 60), (0, y), (WIDTH, y))

        max_vis = max(10, self.map_data["max_level_reached"] + 3)
        
        # 2. Líneas de Ruta
        for lvl in range(1, max_vis):
            p1 = self.get_map_node_pos(lvl)
            p2 = self.get_map_node_pos(lvl+1)
            p1 = (p1[0] + self.map_scroll_x, p1[1])
            p2 = (p2[0] + self.map_scroll_x, p2[1])
            
            if lvl < self.map_data["max_level_reached"]: pygame.draw.line(self.screen, (100, 255, 150), p1, p2, 6) # Completado
            else: pygame.draw.line(self.screen, (60, 60, 80), p1, p2, 6) # Bloqueado

        # 3. Nodos
        t = pygame.time.get_ticks()
        for lvl in range(1, max_vis + 1):
            x, y = self.get_map_node_pos(lvl)
            x += self.map_scroll_x
            
            is_boss = (lvl % 10 == 0)
            base_size = 20 if is_boss else 12
            color = (150, 150, 150)
            
            if lvl == self.map_data["current_node"]:
                color = (255, 255, 0)
                pulse = base_size + 5 + math.sin(t / 150) * 5
                pygame.draw.circle(self.screen, (255, 255, 0, 100), (x, y), pulse, 2)
            elif lvl <= self.map_data["max_level_reached"]: color = (0, 200, 255)
            elif is_boss: color = (200, 50, 50)
            else: color = (50, 50, 50)

            pygame.draw.circle(self.screen, color, (x, y), base_size)
            if is_boss:
                pygame.draw.circle(self.screen, (0,0,0), (x,y), base_size-4)
                pygame.draw.circle(self.screen, color, (x,y), base_size-8)
            
            txt = self.ui_font.render(str(lvl), True, (255,255,255))
            self.screen.blit(txt, (x - txt.get_width()//2, y - base_size - 25))

        # 4. UI del Mapa
        title = self.font.render("SELECTOR DE NIVELES [Flechas: Mover | ENTER: Jugar | M: Tienda]", True, (255, 255, 255))
        self.screen.blit(title, (20, 20))
        ui_txt = self.font.render(f"Monedas: {self.player.inv['coins']} | HP: {self.player.inv['hp']}/{self.player.inv['max_hp']}", True, (255, 215, 0))
        self.screen.blit(ui_txt, (20, 60))

    def draw_menu(self):
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA); overlay.fill((0, 0, 0, 220))
        self.screen.blit(overlay, (0, 0))

        if self.state == "PAUSED":
            title = self.title_font.render("PAUSA", True, (255, 255, 255))
            self.menu_options = ["Continuar", "Tienda", "Salir al Mapa", "Borrar Datos"]
            self.screen.blit(title, (WIDTH//2 - title.get_width()//2, 100))
            for i, opt in enumerate(self.menu_options):
                color = (255, 255, 100) if i == self.menu_selected else (180, 180, 180)
                text = self.font.render(opt, True, color)
                if i == self.menu_selected: self.screen.blit(self.font.render(">", True, color), (WIDTH//2 - text.get_width()//2 - 30, 220 + i * 60))
                self.screen.blit(text, (WIDTH//2 - text.get_width()//2, 220 + i * 60))

        elif self.state == "CONFIRM_DELETE":
            title = self.title_font.render("¿BORRAR PROGRESO?", True, (255, 100, 100))
            self.menu_options = ["Cancelar", "Sí, borrar todo"]
            self.screen.blit(title, (WIDTH//2 - title.get_width()//2, 150))
            for i, opt in enumerate(self.menu_options):
                color = (255, 255, 100) if i == self.menu_selected else (180, 180, 180)
                text = self.font.render(opt, True, color)
                if i == self.menu_selected: self.screen.blit(self.font.render(">", True, color), (WIDTH//2 - text.get_width()//2 - 30, 280 + i * 60))
                self.screen.blit(text, (WIDTH//2 - text.get_width()//2, 280 + i * 60))

        elif self.state == "SHOP":
            shop_rect = pygame.Rect(40, 40, WIDTH - 80, HEIGHT - 80)
            pygame.draw.rect(self.screen, (30, 30, 45), shop_rect, border_radius=15)
            pygame.draw.rect(self.screen, (255, 215, 0), shop_rect, 4, border_radius=15)

            self.screen.blit(self.title_font.render("TIENDA & EQUIPO", True, (255, 215, 0)), (WIDTH//2 - 200, 50))
            self.screen.blit(self.font.render(f"Monedas: {self.player.inv['coins']}", True, (255, 215, 0)), (WIDTH - 250, 60))

            start_x, start_y = 70, 120
            col_width, row_height = 330, 60
            
            for i, item in enumerate(SHOP_ITEMS):
                x = start_x + (i % 2) * col_width
                y = start_y + (i // 2) * row_height
                is_selected = (i == self.menu_selected)
                
                box_rect = pygame.Rect(x, y, col_width - 15, row_height - 10)
                pygame.draw.rect(self.screen, (60, 60, 90) if is_selected else (40, 40, 55), box_rect, border_radius=8)
                if is_selected: pygame.draw.rect(self.screen, (255, 255, 100), box_rect, 2, border_radius=8)

                if item["tex"] in TEXTURES: self.screen.blit(pygame.transform.scale(TEXTURES[item["tex"]], (24, 24)), (x + 10, y + 12))

                color = (255, 255, 255)
                status = f"${item['cost']}" if item['cost'] > 0 else ""
                inv = self.player.inv
                bought = False

                if item["id"] in ["gun", "rifle", "rpg"]:
                    if inv.get(f"owns_{item['id']}"): 
                        bought = True
                        status = "EQUIPADO" if inv["weapon"] == item["id"] else "EQUIPAR"
                        color = (100, 255, 100) if inv["weapon"] == item["id"] else (200, 200, 200)
                else:
                    if (item["id"] == "magnet" and inv.get("has_magnet")) or \
                       (item["id"] == "speed_boots" and inv.get("has_speed")) or \
                       (item["id"] == "extra_jump" and inv["max_jumps"] >= 3) or \
                       (item["id"] == "shield" and inv.get("has_shield")) or \
                       (item["id"] == "double_coin" and inv.get("double_coin")):
                        bought, status, color = True, "(OK)", (100, 100, 100)
                
                if not bought and item["cost"] > 0 and inv["coins"] < item["cost"]: color = (200, 100, 100)

                self.screen.blit(self.ui_font.render(item["name"], True, color), (x + 45, y + 14))
                cost_txt = self.ui_font.render(status, True, color)
                self.screen.blit(cost_txt, (x + col_width - 30 - cost_txt.get_width(), y + 14))

            desc_panel = pygame.Rect(70, HEIGHT - 90, WIDTH - 140, 40)
            pygame.draw.rect(self.screen, (20, 20, 30), desc_panel, border_radius=8)
            desc_txt = self.ui_font.render(SHOP_ITEMS[self.menu_selected].get("desc", ""), True, (200, 200, 200))
            self.screen.blit(desc_txt, (WIDTH//2 - desc_txt.get_width()//2, HEIGHT - 80))

    def draw_ui(self):
        ui_panel = pygame.Surface((200, 130), pygame.SRCALPHA)
        pygame.draw.rect(ui_panel, (0, 0, 0, 140), (0, 0, 200, 130), border_radius=12)
        self.screen.blit(ui_panel, (15, 15))

        self.screen.blit(pygame.transform.scale(TEXTURES["coin"], (24, 24)), (25, 25))
        self.screen.blit(self.ui_font.render(f"x {self.player.inv['coins']}", True, (255, 215, 0)), (55, 27))

        heart, heart_e = pygame.transform.scale(TEXTURES["heart"], (22, 22)), pygame.transform.scale(TEXTURES["heart_empty"], (22, 22))
        for i in range(self.player.inv["max_hp"]):
            x_pos, y_pos = 25 + ((i % 6) * 26), 55 + ((i // 6) * 26)
            self.screen.blit(heart if i < self.player.inv["hp"] else heart_e, (x_pos, y_pos))

        y_offset = 55 + (((self.player.inv["max_hp"] - 1) // 6) * 26) + 30
        draw_x = 25
        
        # Arma actual
        wpn = self.player.inv["weapon"]
        if wpn in TEXTURES:
            self.screen.blit(pygame.transform.scale(TEXTURES[wpn], (24, 24)), (draw_x, y_offset)); draw_x += 30

        # Powerups
        for key, tex in [("has_magnet", "magnet"), ("has_speed", "boots"), ("has_shield", "shield"), ("double_coin", "double_coin")]:
            if self.player.inv.get(key): self.screen.blit(pygame.transform.scale(TEXTURES[tex], (20, 20)), (draw_x, y_offset)); draw_x += 25
        if self.player.inv["max_jumps"] >= 3: self.screen.blit(pygame.transform.scale(TEXTURES["spring"], (20, 20)), (draw_x, y_offset)); draw_x += 25

        # Boss HP
        for b in self.bosses:
            pygame.draw.rect(self.screen, (100, 0, 0), (WIDTH//2 - 200, 20, 400, 20))
            pygame.draw.rect(self.screen, (255, 0, 0), (WIDTH//2 - 200, 20, 400 * (max(0, b.hp) / b.max_hp), 20))
            b_txt = self.font.render("JEFE DE ZONA", True, (255, 255, 255))
            self.screen.blit(b_txt, (WIDTH//2 - b_txt.get_width()//2, 22))

    def run(self):
        while True:
            mouse_click = False
            menu_move, menu_select, menu_cancel = 0, False, False

            for event in pygame.event.get():
                if event.type == pygame.QUIT: self.save_game(); pygame.quit(); sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: mouse_click = True
                
                if event.type == pygame.KEYDOWN:
                    if self.state == "PLAYING" and event.key == pygame.K_ESCAPE: self.state = "PAUSED"; self.menu_selected = 0
                    elif self.state == "MAP":
                        if event.key in (pygame.K_RIGHT, pygame.K_d) and self.map_data["current_node"] < self.map_data["max_level_reached"]: self.map_data["current_node"] += 1
                        if event.key in (pygame.K_LEFT, pygame.K_a) and self.map_data["current_node"] > 1: self.map_data["current_node"] -= 1
                        if event.key in (pygame.K_RETURN, pygame.K_SPACE): self.load_level(self.map_data["current_node"]); self.state = "PLAYING"
                        if event.key == pygame.K_m: self.state = "SHOP"; self.menu_options = SHOP_ITEMS; self.menu_selected = 0 # Tienda desde mapa
                    elif self.state != "PLAYING":
                        if event.key in (pygame.K_UP, pygame.K_w): menu_move = -2 if self.state == "SHOP" else -1
                        elif event.key in (pygame.K_DOWN, pygame.K_s): menu_move = 2 if self.state == "SHOP" else 1
                        elif event.key in (pygame.K_LEFT, pygame.K_a) and self.state == "SHOP": menu_move = -1
                        elif event.key in (pygame.K_RIGHT, pygame.K_d) and self.state == "SHOP": menu_move = 1
                        elif event.key in (pygame.K_RETURN, pygame.K_SPACE): menu_select = True
                        elif event.key == pygame.K_ESCAPE: menu_cancel = True

            if self.state == "PLAYING":
                if mouse_click: self.shoot(pygame.mouse.get_pos())

                self.player.update(self.walls)
                self.enemies.update(self.walls)
                self.bosses.update(self.walls, self.player)
                self.camera.update(self.player)

                # Balística
                for proj in list(self.projectiles):
                    hit_w = proj.update(self.walls)
                    hit_e = pygame.sprite.spritecollide(proj, self.enemies, False)
                    hit_b = pygame.sprite.spritecollide(proj, self.bosses, False)
                    if hit_e or hit_b or hit_w:
                        if proj.type == "rpg":
                            exp = Explosion(proj.rect.centerx, proj.rect.centery)
                            self.explosions.add(exp); self.all_sprites.add(exp)
                        else:
                            for e in hit_e: e.hp -= proj.damage
                            for b in hit_b: b.hp -= proj.damage
                        if not hit_w: proj.kill()

                self.explosions.update(self.walls)
                for exp in self.explosions:
                    for e in self.enemies:
                        if exp.rect.colliderect(e.rect): e.hp -= 0.5
                    for b in self.bosses:
                        if exp.rect.colliderect(b.rect): b.hp -= 0.5

                for e in list(self.enemies):
                    if e.hp <= 0: e.kill(); self.player.inv["coins"] += 1
                for b in list(self.bosses):
                    if b.hp <= 0:
                        b.kill(); self.player.inv["coins"] += 50
                        obj = StaticObject(b.rect.centerx, b.rect.bottom - 32, "door")
                        self.doors.add(obj); self.all_sprites.add(obj)

                # Imán
                if self.player.inv.get("has_magnet"):
                    for coin in self.coins:
                        dx, dy = self.player.rect.centerx - coin.rect.centerx, self.player.rect.centery - coin.rect.centery
                        dist = (dx**2 + dy**2)**0.5
                        if 0 < dist < 120:
                            coin.rect.x += int((dx / dist) * 5)
                            coin.rect.y += int((dy / dist) * 5)

                if pygame.sprite.spritecollide(self.player, self.coins, True): 
                    self.player.inv["coins"] += (2 if self.player.inv.get("double_coin") else 1)
                if pygame.sprite.spritecollide(self.player, self.keys, True): self.player.inv["keys"] += 1
                if pygame.sprite.spritecollideany(self.player, self.trampolines): self.player.vel.y = -20; self.player.jumps = 1
                
                if pygame.sprite.spritecollideany(self.player, self.enemies) or pygame.sprite.spritecollideany(self.player, self.bosses): self.take_damage()
                for spike in self.spikes:
                    if self.player.rect.colliderect(spike.hitbox): self.take_damage()

                # --- FIX DE LA PUERTA Y LA LLAVE ---
                if pygame.sprite.spritecollideany(self.player, self.doors):
                    is_boss_level = (self.map_data["current_node"] % 10 == 0)
                    
                    if self.player.inv["keys"] > 0 or is_boss_level:
                        if not is_boss_level:
                            self.player.inv["keys"] -= 1 # Gastar llave
                            
                        if self.map_data["current_node"] == self.map_data["max_level_reached"]: 
                            self.map_data["max_level_reached"] += 1
                            
                        self.map_data["current_node"] = self.map_data["max_level_reached"]
                        self.save_game(); self.state = "MAP"
                    else:
                        # Empujar hacia atrás si no hay llave
                        self.player.rect.x -= self.player.facing * 5

                self.screen.fill(COLOR_BG)
                for s in self.all_sprites: self.screen.blit(s.image, self.camera.apply(s))
                self.screen.blit(self.player.image, self.camera.apply(self.player))
                self.draw_ui()

            elif self.state == "MAP": self.draw_map()
            else:
                self.handle_menu_input(menu_move, menu_select, menu_cancel)
                if self.state in ["PAUSED", "CONFIRM_DELETE", "SHOP"]:
                    self.screen.fill(COLOR_BG) # Fondo base por si acaso
                    for s in self.all_sprites: self.screen.blit(s.image, self.camera.apply(s))
                    self.draw_ui()
                    self.draw_menu()
                elif self.state == "MAP": self.draw_map() # Transición rápida

            pygame.display.flip()
            self.clock.tick(FPS)

if __name__ == "__main__":
    Game().run()