# YOU DONT NEED TO MODIFY OR READ ANY CODE WITHIN THIS FILE
# YOU DONT NEED TO MODIFY OR READ ANY CODE WITHIN THIS FILE
# YOU DONT NEED TO MODIFY OR READ ANY CODE WITHIN THIS FILE
# YOU DONT NEED TO MODIFY OR READ ANY CODE WITHIN THIS FILE
# YOU DONT NEED TO MODIFY OR READ ANY CODE WITHIN THIS FILE
# YOU DONT NEED TO MODIFY OR READ ANY CODE WITHIN THIS FILE
# YOU DONT NEED TO MODIFY OR READ ANY CODE WITHIN THIS FILE
# YOU DONT NEED TO MODIFY OR READ ANY CODE WITHIN THIS FILE
# YOU DONT NEED TO MODIFY OR READ ANY CODE WITHIN THIS FILE
# YOU DONT NEED TO MODIFY OR READ ANY CODE WITHIN THIS FILE
# YOU DONT NEED TO MODIFY OR READ ANY CODE WITHIN THIS FILE






























import pygame
class TonyStank:
    def __init__(self):
        self.fillColor = (255, 255, 255)
        self.strokeColor = (0, 0, 0)
        self.strokeWeight = 1
        self.noStroke = False
        self.noFill = False
        self.polyPoints = []
        self.drawingPoly = False
        self.screen = None


tonyStank = TonyStank()


def parseColorRGB(r, g, b):
    return (r, g, b)


def parseColorGrey(g):
    return (g, g, g)


def background(r, g=None, b=0):
    global tonyStank
    if g == None:
        tonyStank.screen.fill(parseColorGrey(r))
        return
    tonyStank.screen.fill(parseColorRGB(r, g, b))


def fill(r, g=None, b=0):
    global tonyStank
    if g == None:
        tonyStank.fillColor = parseColorGrey(r)
        return
    tonyStank.noFill = False
    tonyStank.fillColor = parseColorRGB(r, g, b)

def stroke(r, g=None, b=0):
    global tonyStank
    if g == None:
        tonyStank.strokeColor = parseColorGrey(r)
        return
    tonyStank.noFill = False
    tonyStank.strokeColor = parseColorRGB(r, g, b)


def noFill():
    tonyStank.noFill = True


def rect(x, y, w, h):
    global tonyStank
    if not tonyStank.noFill:
        pygame.draw.rect(tonyStank.screen, tonyStank.fillColor, (x, y, w, h))
    if tonyStank.noStroke:
        return
    pygame.draw.rect(tonyStank.screen, tonyStank.strokeColor, (x, y, w, h), width=tonyStank.strokeWeight)


def ellipse(x, y, w, h):
    global tonyStank
    if not tonyStank.noFill:
        pygame.draw.ellipse(tonyStank.screen, tonyStank.fillColor, (x, y, w, h))
    if tonyStank.noStroke:
        return
    pygame.draw.ellipse(tonyStank.screen, tonyStank.strokeColor, (x, y, w, h), width=tonyStank.strokeWeight)


def circle(x, y, size):
    ellipse(x, y, size, size)


def line(x1, y1, x2, y2):
    global tonyStank
    if tonyStank.noStroke:
        return
    pygame.draw.line(tonyStank.screen, tonyStank.strokeColor, (x1, y1), (x2, y2), width=tonyStank.strokeWeight)


def beginShape():
    global tonyStank
    if tonyStank.drawingPoly:
        raise Exception("Already drawing a shape!")
        return
    tonyStank.drawingPoly = True


def vertex(x, y):
    global tonyStank
    if not tonyStank.drawingPoly:
        raise Exception("Not drawing a shape!")
        return
    tonyStank.polyPoints.append((x, y))


def endShape():
    global tonyStank
    if not tonyStank.drawingPoly:
        raise Exception("Not drawing a shape!")
        return
    if not tonyStank.noFill:
        pygame.draw.polygon(tonyStank.screen, tonyStank.fillColor, tonyStank.polyPoints)
    if tonyStank.noStroke:
        return
    pygame.draw.polygon(tonyStank.screen, tonyStank.strokeColor, tonyStank.polyPoints, width=tonyStank.strokeWeight)
    tonyStank.polyPoints = []
    tonyStank.drawingPoly = False


def run(setup, draw):
    pygame.init()
    WIDTH, HEIGHT = 500, 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    tonyStank.screen = screen
    pygame.display.set_caption("Sketch")
    clock = pygame.time.Clock()

    setup()
    running = True
    background(127)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()