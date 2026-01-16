from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

blocks = []

def game():
    app = Ursina()
    player = FirstPersonController()

    Sky()

    for i in range(20):
        for j in range(20):
            block = Button(color=color.white, model='cube', position=(j, 0, i), texture='grass.png', parent=scene, origin_y=0.5)
            blocks.append(block)

    app.run()

def input(key):
    if key == 'escape':
        quit()

    for block in blocks:
        if block.hovered:
            if key == 'right mouse down':
                new = Button(color=color.white, model="cube", position=block.position + mouse.normal, texture='grass.png', parent=scene, origin_y=0.5)
                blocks.append(new)
            if key == 'left mouse down':
                blocks.remove(block)
                destroy(block)


if __name__ == '__main__':
    print("Running as main script")
    game()