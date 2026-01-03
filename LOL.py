#setting up uniscript interpreter
from ursina import Ursina, Entity, color, Sky, held_keys, time
from ursina.prefabs.first_person_controller import FirstPersonController
print("Welcome to uniscript!😄")
print("This coding language ensures making games and programs is easy and fun!")
print("to exit uniscript, press ctrl+shift+alt+q")
#interpreter
code=input(":")
if code=="input=draw(tree)+[assign_player+view=first person]+{controls=w,s,a,d}":
    app=Ursina()
    Sky()
    tree_top=Entity(model='sphere',color=color.green,scale=(5,4,6),position=(1,3,1))
    trunk=Entity(model='cube',color=color.brown,scale=(1,3,1),position=(1,1,1))
    ground = Entity(model='plane', scale=(500,500,500), color=color.gray, collider='box')
    player_controller=FirstPersonController()
    app.run()
elif code=="input=draw(cube tree)+[assign_player+view=first person]+{controls=w,s,a,d}":
    app=Ursina()
    Sky()
    tree_top=Entity(model='cube',color=color.green,scale=(2,4,2),position=(1,3,1))
    trunk=Entity(model='cube',color=color.brown,scale=(1,3,1),position=(1,1,1))
    ground = Entity(model='plane', scale=(500,500,500), color=color.gray, collider='box')
    player_controller=FirstPersonController()
    app.run()
#houses
elif code=="input=draw(house)+[assign_player+view=first person]+{controls=w,s,a,d}":
    app=Ursina()
    Sky()
    house_body=Entity(model='cube',color=color.yellow,scale=(4,3,4),position=(-2,1,1))
    roof=Entity(model='plane',color=color.red,scale=(4.5,2,4.5),position=(-2,4,1))
    door=Entity(model='cube',color=color.brown,scale=(1,2,0.1),position=(-2,0.5,3))
    ground = Entity(model='plane', scale=(500,500,500), color=color.gray, collider='box')
    player_controller=FirstPersonController()
    app.run()
elif code=="input=draw(chair)+[assign_player+view=first person]+{controls=w,s,a,d}":
    app=Ursina()
    Sky()
    chair_seat=Entity(model='cube',color=color.brown,scale=(1.5,0.2,1.5),position=(0,0.5,0))
    chair_back=Entity(model='cube',color=color.brown,scale=(1.5,1.5,0.2),position=(0,1.25,-0.25))
    chair_leg1=Entity(model='cube',color=color.brown,scale=(0.2,0.5,0.2),position=(-0.75,0.25,-0.25))
    chair_leg2=Entity(model='cube',color=color.brown,scale=(0.2,0.5,0.2),position=(0.75,0.25,-0.25))
    chair_leg3=Entity(model='cube',color=color.brown,scale=(0.2,0.5,0.2),position=(-0.75,0.25,0.75))
    chair_leg4=Entity(model='cube',color=color.brown,scale=(0.2,0.5,0.2),position=(0.75,0.25,0.75))
    ground = Entity(model='plane', scale=(500,500,500), color=color.gray, collider='box')
    player_controller=FirstPersonController()
    app.run()
elif code=="input=draw(chair.color=blue)+[assign_player+view=first person]+{controls=w,s,a,d}":
    app=Ursina()
    Sky()
    chair_seat=Entity(model='cube',color=color.blue,scale=(1.5,0.2,1.5),position=(0,0.5,0))
    chair_back=Entity(model='cube',color=color.blue,scale=(1.5,1.5,0.2),position=(0,1.25,-0.25))
    chair_leg1=Entity(model='cube',color=color.blue,scale=(0.2,0.5,0.2),position=(-0.75,0.25,-0.25))
    chair_leg2=Entity(model='cube',color=color.blue,scale=(0.2,0.5,0.2),position=(0.75,0.25,-0.25))
    chair_leg3=Entity(model='cube',color=color.blue,scale=(0.2,0.5,0.2),position=(-0.75,0.25,0.75))
    chair_leg4=Entity(model='cube',color=color.blue,scale=(0.2,0.5,0.2),position=(0.75,0.25,0.75))
    ground = Entity(model='plane', scale=(500,500,500), color=color.gray, collider='box')
    player_controller=FirstPersonController()
    app.run()
elif code=="input=draw(skyscraper)+[assign_player+view=first person]+{controls=w,s,a,d}":
    app=Ursina()
    Sky()
    skyscraper = Entity(model='cube', color=color.gray, scale=(3,15,3), position=(0,7.5,0))
    door = Entity(model='cube', color=color.brown, scale=(1,2,0.1), position=(0,1,1.55))
    for i in range(2):
        window=Entity(model='cube', color=color.blue, scale=(0.5,0.5,0.1), position=(1,3+i*3,1.55))
        window2=Entity(model='cube', color=color.blue, scale=(0.5,0.5,0.1), position=(-1,3+i*3,1.55))
        window3=Entity(model='cube', color=color.blue, scale=(0.5,0.5,0.1), position=(0,3+i*3,1.55))
    ground = Entity(model='plane', scale=(500,500,500), color=color.gray, collider='box')
    player_controller=FirstPersonController()
    app.run()
elif code=="input=draw(cube tree)+{house}+[assign_player+view=first person]+{controls=w,s,a,d}":
    app=Ursina()
    Sky()
    tree_top=Entity(model='cube',color=color.green,scale=(2,4,2),position=(3,2,3))
    trunk=Entity(model='cube',color=color.brown,scale=(1,3,1),position=(3,1,3))
    house_body=Entity(model='cube',color=color.brown,scale=(4,3,4),position=(-3,1,3))
    roof=Entity(model='plane',color=color.red,scale=(4.5,2,4.5),position=(-3,4,3))
    door=Entity(model='cube',color=color.dark_gray,scale=(1,2,0.1),position=(-3,0.5,5))
    ground = Entity(model='plane', scale=(500,500,500), color=color.gray, collider='box')
    player_controller=FirstPersonController()
    app.run()
elif code=="input=draw(forest)+[assign_player+view=first person]+{controls=w,s,a,d}":
    app=Ursina()
    Sky()
    for x in range(-10,11,5):
        for z in range(-10,11,5):
            tree_top=Entity(model='sphere',color=color.green,scale=(2,4,2),position=(x,3,z))
            trunk=Entity(model='cube',color=color.brown,scale=(0.5,3,0.5),position=(x,1.5,z))
    ground = Entity(model='plane', scale=(500,500,500), color=color.gray, collider='box')
    player_controller=FirstPersonController()
    app.run()
elif code=="input=draw(bed)+[assign_player+view=first person]+{controls=w,s,a,d}":
    app=Ursina()
    Sky()
    bed_base=Entity(model='cube',color=color.white,scale=(3,0.5,6),position=(0,0.25,0))
    bed_headboard=Entity(model='cube',color=color.brown,scale=(3,2,0.2),position=(0,1.25,-2.9))
    bed_pillow=Entity(model='cube',color=color.light_gray,scale=(2,0.5,1),position=(0,0.75,-2))
    ground = Entity(model='plane', scale=(500,500,500), color=color.gray, collider='box')
    player_controller=FirstPersonController()
    app.run()
#grounds
elif code=="input=draw(house).ground==field+[assign_player+view=first person]+{controls=w,s,a,d}":
    app=Ursina()
    Sky()
    house_body=Entity(model='cube',color=color.yellow,scale=(4,3,4),position=(-2,1,1))
    roof=Entity(model='plane',color=color.red,scale=(4.5,2,4.5),position=(-2,4,1))
    door=Entity(model='cube',color=color.brown,scale=(1,2,0.1),position=(-2,0.5,3))
    ground = Entity(model='plane', scale=(500,500,500), color=color.green, collider='box')
    player_controller=FirstPersonController()
    app.run()
elif code=="input=draw(cactus).ground==desert+[assign_player+view=first person]+{controls=w,s,a,d}":
    app=Ursina()
    Sky()
    cactus_body=Entity(model='cube',color=color.green,scale=(1,4,1),position=(0,2,0))
    cactus_arm1=Entity(model='cube',color=color.green,scale=(0.5,2,0.5),position=(-0.75,3,0))
    cactus_arm2=Entity(model='cube',color=color.green,scale=(0.5,2,0.5),position=(0.75,3,0))
    ground = Entity(model='plane', scale=(500,500,500), color=color.yellow, collider='box')
    player_controller=FirstPersonController()
    app.run()
elif code=="input=draw(snowman).ground==snow+[assign_player+view=first person]+{controls=w,s,a,d}":
    app=Ursina()
    Sky()
    snowman_base=Entity(model='sphere',color=color.white,scale=(2,2,2),position=(0,1,0))
    snowman_middle=Entity(model='sphere',color=color.white,scale=(1.5,1.5,1.5),position=(0,3,0))
    snowman_head=Entity(model='sphere',color=color.white,scale=(1,1,1),position=(0,4.5,0))
    snowman_eyes=Entity(model='sphere',color=color.black,scale=(0.1,0.1,0.1),position=(-0.2,5,0.5))
    snowman_eyes2=Entity(model='sphere',color=color.black,scale=(0.1,0.1,0.1),position=(0.2,5,0.5))
    snowman_nose=Entity(model='cube',color=color.orange,scale=(0.1,0.5,0.1),position=(0,4.8,0.6),rotation=(90,0,0)) 
    ground = Entity(model='plane', scale=(500,500,500), color=color.light_gray, collider='box')
    player_controller=FirstPersonController()
    app.run()
#textures
elif code=="input=draw(ground.texture=grass)+{house}+[assign_player+view=first person]+{controls=w,s,a,d}":
    app=Ursina()
    Sky()
    house_body=Entity(model='cube',color=color.yellow,scale=(4,3,4),position=(-2,1,1))
    roof=Entity(model='plane',color=color.red,scale=(4.5,2,4.5),position=(-2,4,1))
    door=Entity(model='cube',color=color.brown,scale=(1,2,0.1),position=(-2,0.5,3))
    ground = Entity(model='plane', texture='grass', scale=(500,500,500), collider='box')
    player_controller=FirstPersonController()
    app.run()
#combos
elif code=="input=draw(house)+{tree}+[assign_player+view=first person]+{controls=w,s,a,d}":
    app=Ursina()
    Sky()
    house_body=Entity(model='cube',color=color.yellow,scale=(4,3,4),position=(-2,1,1))
    roof=Entity(model='plane',color=color.red,scale=(4.5,2,4.5),position=(-2,4,1))
    door=Entity(model='cube',color=color.brown,scale=(1,2,0.1),position=(-2,0.5,3))
    tree_top=Entity(model='sphere',color=color.green,scale=(5,4,6),position=(3,3,1))
    trunk=Entity(model='cube',color=color.brown,scale=(1,3,1),position=(3,1,1))
    ground = Entity(model='plane', scale=(500,500,500), color=color.gray, collider='box')
    player_controller=FirstPersonController()
    app.run()   
elif code=="input=draw(skyscraper)+{house}+{tree}+[assign_player+view=first person]+{controls=w,s,a,d}":
    app=Ursina()
    Sky()
    skyscraper = Entity(model='cube', color=color.gray, scale=(3,15,3), position=(0,7.5,0))
    door = Entity(model='cube', color=color.brown, scale=(1,2,0.1), position=(0,1,1.55))
    for i in range(2):
        window=Entity(model='cube', color=color.blue, scale=(0.5,0.5,0.1), position=(1,3+i*3,1.55))
        window2=Entity(model='cube', color=color.blue, scale=(0.5,0.5,0.1), position=(-1,3+i*3,1.55))
        window3=Entity(model='cube', color=color.blue, scale=(0.5,0.5,0.1), position=(0,3+i*3,1.55))
    house_body=Entity(model='cube',color=color.yellow,scale=(4,3,4),position=(-5,1,3))
    roof=Entity(model='plane',color=color.red,scale=(4.5,2,4.5),position=(-5,4,3))
    door_house=Entity(model='cube',color=color.brown,scale=(1,2,0.1),position=(-5,0.5,5))
    tree_top=Entity(model='sphere',color=color.green,scale=(2,4,2),position=(5,3,3))
    trunk=Entity(model='cube',color=color.brown,scale=(1,3,1),position=(5,1,3))
    ground = Entity(model='plane', scale=(500,500,500), color=color.green, collider='box')
    player_controller=FirstPersonController()
    app.run()
elif code=="input=draw(house)+{chair}+[assign_player+view=first person]+{controls=w,s,a,d}":
    app=Ursina()
    Sky()
    house_body=Entity(model='cube',color=color.yellow,scale=(4,3,4),position=(-2,1,1))
    roof=Entity(model='plane',color=color.red,scale=(4.5,2,4.5),position=(-2,4,1))
    door=Entity(model='cube',color=color.brown,scale=(1,2,0.1),position=(-2,0.5,3))
    chair_seat=Entity(model='cube',color=color.brown,scale=(1.5,0.2,1.5),position=(2,0.5,1))
    chair_back=Entity(model='cube',color=color.brown,scale=(1.5,1.5,0.2),position=(2,1.25,0.25))
    chair_leg1=Entity(model='cube',color=color.brown,scale=(0.2,0.5,0.2),position=(1.25,0.25,0.25))
    chair_leg2=Entity(model='cube',color=color.brown,scale=(0.2,0.5,0.2),position=(2.75,0.25,0.25))
    chair_leg3=Entity(model='cube',color=color.brown,scale=(0.2,0.5,0.2),position=(1.25,0.25,1.75))
    chair_leg4=Entity(model='cube',color=color.brown,scale=(0.2,0.5,0.2),position=(2.75,0.25,1.75))
    ground = Entity(model='plane', scale=(500,500,500), color=color.gray, collider='box')
    player_controller=FirstPersonController()
    app.run()
    #merges
elif code=="input=merge(draw(lake)+{forest}+[assign_player+view=first person]+{controls=w,s,a,d})+(input=draw(skyscraper)+[assign_player+view=first person]+{controls=w,s,a,d}))":
    app=Ursina()
    Sky()
    lake=Entity(model='plane',color=color.blue,scale=(5,5,5),position=(13,0,13))
    for x in range(-10,11,5):
        for z in range(-10,11,5):
            tree_top=Entity(model='sphere',color=color.green,scale=(2,4,2),position=(x,3,z))
            trunk=Entity(model='cube',color=color.brown,scale=(0.5,3,0.5),position=(x,1.5,z))
            ground = Entity(model='plane', scale=(500,500,500), color=color.gray, collider='box')
            skyscraper = Entity(model='cube', color=color.gray, scale=(3,15,3), position=(0,7.5,0))
    door = Entity(model='cube', color=color.brown, scale=(1,2,0.1), position=(0,1,1.55))
    for i in range(2):
        window=Entity(model='cube', color=color.blue, scale=(0.5,0.5,0.1), position=(1,3+i*3,1.55))
        window2=Entity(model='cube', color=color.blue, scale=(0.5,0.5,0.1), position=(-1,3+i*3,1.55))
        window3=Entity(model='cube', color=color.blue, scale=(0.5,0.5,0.1), position=(0,3+i*3,1.55))
    ground = Entity(model='plane', scale=(500,500,500), color=color.gray, collider='box')
    player_controller=FirstPersonController()
    app.run()
elif code=="input=merge(input=draw(chair)+[assign_player+view=first person]+{controls=w,s,a,d}+input=draw(bed)+[assign_player+view=first person]+{controls=w,s,a,d})":
    app=Ursina()
    Sky()
    chair_seat=Entity(model='cube',color=color.brown,scale=(1.5,0.2,1.5),position=(2,0.5,1))
    chair_back=Entity(model='cube',color=color.brown,scale=(1.5,1.5,0.2),position=(2,1.25,0.25))
    chair_leg1=Entity(model='cube',color=color.brown,scale=(0.2,0.5,0.2),position=(1.25,0.25,0.25))
    chair_leg2=Entity(model='cube',color=color.brown,scale=(0.2,0.5,0.2),position=(2.75,0.25,0.25))
    chair_leg3=Entity(model='cube',color=color.brown,scale=(0.2,0.5,0.2),position=(1.25,0.25,1.75))
    chair_leg4=Entity(model='cube',color=color.brown,scale=(0.2,0.5,0.2),position=(2.75,0.25,1.75))
    bed_base=Entity(model='cube',color=color.white,scale=(3,0.5,6),position=(-5,0.25,1))
    bed_headboard=Entity(model='cube',color=color.brown,scale=(3,2,0.2),position=(-5,1.25,-2.9))
    bed_pillow=Entity(model='cube',color=color.light_gray,scale=(2,0.5,1),position=(-5,0.75,-2))
    ground = Entity(model='plane', scale=(500,500,500), color=color.green, collider='box')
    player_controller=FirstPersonController()
    app.run()
#set_types
elif code=="set house_type=(hut)+[assign_player+view=first person]+{controls=w,s,a,d}":
    app=Ursina()
    Sky()
    house_body=Entity(model='cube',color=color.brown,scale=(4,3,4),position=(-3,1,3))
    roof=Entity(model='plane',color=color.red,scale=(4.5,2,4.5),position=(-3,4,3))
    door=Entity(model='cube',color=color.dark_gray,scale=(1,2,0.1),position=(-3,0.5,5))
    ground = Entity(model='plane', scale=(500,500,500), color=color.gray, collider='box')
    player_controller=FirstPersonController()
    app.run()
elif code=="report issue":
    print("To report an issue, please visit our GitHub page at https://github.com/your-repo/issues (this is a placeholder link).")
elif code=="import_drive.input=draw(drone)+[assign_player+drive]+{controls=w,s,a,d}":
    app = Ursina()
    Sky()
    # drone body
    drone_body = Entity(model='cube',color=color.gray,scale=(3,1,2),position=(0,1,0))
    # propellers
    propellers = []
    for x in (-1.2, 1.2):
        for z in (-0.9, 0.9):
            propeller = Entity(model='cube',color=color.black,scale=(0.5,0.5,0.5),position=(x,0.5,z),parent=drone_body)
            propellers.append(propeller)

    ground = Entity(model='plane',scale=(500,500,500),color=color.green,collider='box')

    speed = 5
    turn_speed = 90

    def update():
        if held_keys['w']:
            drone_body.position += drone_body.forward * speed * time.dt
        if held_keys['s']:
            drone_body.position -= drone_body.forward * speed * time.dt
        if held_keys['a']:
            drone_body.rotation_y += turn_speed * time.dt
        if held_keys['d']:
            drone_body.rotation_y -= turn_speed * time.dt
    player_controller=FirstPersonController()
    app.run()
#Profile!
elif code=="view_profile":
    profile=input("Enter your profile name(to make it official): ")
    age=input("Enter your age: ")
    role=input("Enter your role: ")
    joined=input("Enter your join date(DD/MM/YYYY): ")
    print("Profile loaded successfully!")
    print("Profile Name:",profile)
    print("Age:",age)
    print("Role:",role)
    print("Join Date:",joined)
elif  code=="import uni_low,ttr=#00ff00.brown,plyr=entity.dft_view":
    app=Ursina()
    Sky()
    ttr_top=Entity(model='cube',color=color.green,scale=(5,4,6),position=(0,3,0))
    ttr_trunk=Entity(model='cube',color=color.brown,scale=(2,2,2),position=(0,1,0))
    ground = Entity(model='plane', scale=(500,500,500), color=color.gray, collider='box')
    player_controller=FirstPersonController()
    app.run()
else:
    print("*WARNING*: unknown syntax/command")
    Error_system=input("Would you like to switch to default mode? (yes/no): ")
    if Error_system=="yes":
        print("Switching to default. please wait...")
        app=Ursina()
        Sky()
        tree_top=Entity(model='sphere',color=color.green,scale=(5,4,6),position=(1,3,1))
        trunk=Entity(model='cube',color=color.brown,scale=(1,3,1),position=(1,1,1))
        ground = Entity(model='plane', scale=(500,500,500), color=color.gray, collider='box')
        player_controller=FirstPersonController()
        app.run()
    elif Error_system=="no":
        print("loading default cancelled. to exit/restart, rerun the program.")
    else:
        print("Invalid response.")