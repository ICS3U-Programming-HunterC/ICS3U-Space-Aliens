#!/usr/bin/env python
# Created by: Hunter Connolly
# Created on June 2022
# This program is the "Space Aliens" program on the PyBadge

import ugame
import stage

import constants

def game_scene():
    # this function is the main game scene

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    
    # set the backgorund image to 0 in the image bank
    # and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # a sprite that will be updated every frame
    # image at index 5 on (75, 66) on the screen
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

    # create a stage for the background to show up on
    # and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    
    # set the layers of all sprites, items show up in order
    game.layers = [ship] + [background]
    
    # render all sprites
    # most likely you will only render the background once per game scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # button functions
        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT:
            # move the ship to the right 
            # if it hits the border it will stop
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + .15, ship.y)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_LEFT:
            # move ship to the left
            # if it hits the border it will stop
            if ship.x >= 0:
                ship.move(ship.x - .15, ship.y)
            else:  
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass

        # update game logic

        # redraw Sprites
        game.render_sprites([ship])
        game.tick

if __name__ == "__main__":
    game_scene()
