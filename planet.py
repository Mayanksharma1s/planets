import pygame, math
pygame.init()

WIDTH, HEIGHT = 800, 800

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planets | Basfoot")
font = pygame.font.SysFont("comicsans", 19)

class Planet:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 240 / AU # 1 AU = 100 Pixels
    TIMESTEP = 3600*24 # 1 Day time
    
    def __init__(self, x, y, radius, color, mass):   
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.x_vel = 0
        self.y_vel = 0
        self.isSun = False
        self.dist_to_sun = 0
        self.orbit = []

    def draw(self, win):
        x = self.x*self.SCALE + WIDTH/2
        y = self.y*self.SCALE + HEIGHT/2
        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2

                updated_points.append((x,y))


            pygame.draw.lines(win, self.color, False, updated_points, 2)
        
        pygame.draw.circle(win, self.color, (x,y), self.radius)

        if not self.isSun:
            dist_text = font.render(f"{round(self.dist_to_sun/1000, 1)}Km", 1, white)
            win.blit(dist_text, (x - dist_text.get_width()/2,y - dist_text.get_height()/2))

    def force(self, other):
        other_x, other_y = other.x, other.y
        dist_x = other_x - self.x
        dist_y = other_y - self.y
        dist = math.sqrt(dist_x**2 + dist_y**2)

        if other.isSun:
            self.dist_to_sun = dist

        f = self.G * self.mass * other.mass / dist**2

        theta = math.atan2(dist_y, dist_x)
        force_x = math.cos(theta) * f
        force_y = math.sin(theta) * f

        return force_x, force_y
    
    def update_position(self, planets):
        total_fx = total_fy = 0

        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.force(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP

        self.orbit.append((self.x, self.y))


white = (255, 255, 255)
yellow = (255, 254, 0)
blue = (100, 149, 250)
red = (185, 39, 55)
dark_grey = (80, 78, 81)
venus_c = (193, 143, 23)




def main():
    run = True
    clock = pygame.time.Clock()
    

    sun = Planet(0, 0, 30, yellow, 1.98892 * 10**30)
    sun.isSun = True

    earth = Planet(-1*Planet.AU, 0, 16, blue, 5.9742 * 10**24)
    earth.y_vel = 29.783 * 1000
    mars = Planet(-1.5 * Planet.AU, 0, 12, red, 6.39 * 10**23)
    mars.y_vel = 24.077 * 1000
    mercury = Planet(0.387* Planet.AU, 0, 7, dark_grey, 3.30 * 10**23)
    mercury.y_vel = -47.4 * 1000
    venus = Planet(0.723 * Planet.AU, 0, 14, venus_c, 4.8685 * 10**24)
    venus.y_vel = -35.02*1000

    planets = [sun, earth, mars, mercury, venus]
    
    while run:
        clock.tick(60)
        win.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(win)

        pygame.display.update()

    pygame.quit()

main()
