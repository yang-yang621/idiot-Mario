# idiot-Mario

- Student Name:
- Github Username:
- Semester:
- Course:

## Description
This project aims to reproduce a mario like game. This game includes a start menu and a scene with a mario and two enemies. By working on this project, I learnt the general develop process of a game and have a general idea the data structure of a game.
## Key Features
This game has a controlable mario and two enemies that could hurt mario.
## Guide
In order to run this game, `python ./main.py` needs to be run. The first scene is the menu of this game. In this scene, Press Enter can enter the next scene, which is the game scene. In this scene, there is a mario and two enemies. Press left and right to control mario move. If mario hits an enemy, It dies.
## Installation Instructions
This project needs two dependencies, which includes in requirements.txt. These requirements could be installed by running `pip install -r requirements.txt`. 
## Code Review
```python
def move(self, key):
        if key[pg.K_RIGHT]:
            self.walk(direction=True)
        elif key[pg.K_LEFT]:
            self.walk(direction=False)
        elif key[pg.K_UP]:
            self.jump(key)
        else:
            self.x_vel = 0

    
    def walk(self,direction):
        if direction:
            frames = self.right_frames
            self.x_vel = 5
        else:
            frames = self.left_frames
            self.x_vel = -5
        
        if self.frame_index == 0:
            self.frame_index += 1
            self.walk_timer = self.current_time
        else:
            if(self.current_time - self.walk_timer) < 100:
                if self.frame_index < 3:
                    self.frame_index += 1
                else:
                    self.frame_index = 1
                self.walk_timer = self.current_time
        self.image = frames[self.frame_index]
```
This part of code shows how mario actions are handled in this game.  
In move(), input is handled first. direction shows where mario should be heading. If direction is true, mario is heading right, left otherwise. walk() change the the speed of mario and the image of mario so that it looks like walking.
### Major Challenges
The major challenges of this project is getting a deep understand of how game process should work. 
## Example Runs

## Testing

## Missing Features / What's Next
Two features are missing. First , mario can't jump now, so that it can't kill enemies so far. Second, Game scene can't move now, further scene can't be shown. In the next stage, I could add more items like coin box and other enemies. Now the speed on x_axis is fixed, an Accelrate could be added to Mario in the future
## Final Reflection
