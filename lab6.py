GlowScript 2.9 VPython
scene.width=1024
scene.height=760
# CONSTANTS
G = 6.7e-11
mEarth = 6e24
mcraft = 15e3
mMoon = 7e22

deltat = 10
t = 0
pscale = .2
fscale = 2000
dpscale = 40

#OBJECTS AND INITIAL VALUES
Earth = sphere(pos=vector(0,0,0), radius=6.4e6, color=color.cyan)
Moon = sphere(pos=vector(4e8,0,0), radius=1.75e6, color=color.white)
scene.range=11*Earth.radius
# Add a radius for the spacecraft. It should be BIG, so it can be seen.
craft = sphere(pos=vector(-10*Earth.radius,0,0), radius=7e6, color=color.yellow) #crashes: 3.28e3 figure 8-3.275e3
vcraft = vector(0,3.27e3,0)
pcraft = mcraft*vcraft
trail = curve(color=craft.color)    # This creates a trail for the spacecraft
scene.autoscale = 0                 # And this prevents zooming in or out
pArrow = arrow(color=color.green)
print("p=",pcraft)
fArrow = arrow(color=color.cyan)
dpArrow = arrow(color=color.red, opacity=.5)
parArrow = arrow(color=color.orange)
perpArrow = arrow(color=color.purple)

# CALCULATIONS
while t < 10*365*24*60*60:
    scene.center=craft.pos
    scene.range=craft.radius*60
    rate(2000)   # This slows down the animation (runs faster with bigger number)
    # Add statements here for the iterative update of gravitational
    # force, momentum, and position. 
    r = craft.pos - Earth.pos
    rmag = mag(r)
    Fmag = G*mEarth*mcraft/(rmag**2)
    rhat = r/rmag
    Fearth = -Fmag*rhat
    moonmag = mag(craft.pos-Moon.pos)
    # print("Fnet=",Fnet)
    Fmoon = -(G*mcraft*mMoon)/(moonmag**2) * norm(craft.pos-Moon.pos)
    pcraft_i = pcraft + vector(0,0,0)
    Fnet = Fearth + Fmoon
    #Fnet = Fearth
    pcraft = pcraft + Fnet*deltat
    dpcraft = pcraft - pcraft_i
    vcraft = pcraft/mcraft
    craft.pos = craft.pos + vcraft*deltat
    pArrow.pos = craft.pos
    pArrow.axis = pcraft*pscale
    fArrow.pos = craft.pos
    fArrow.axis = Fnet * fscale
    dpArrow.pos = craft.pos
    dpArrow.axis = dpcraft * dpscale
    Fpar = (dot(Fnet, pcraft)*pcraft)/mag(pcraft)**2
    Fperp = Fnet - Fpar
    parArrow.pos = craft.pos
    parArrow.axis = Fpar*pscale*1000000
    perpArrow.pos = craft.pos
    perpArrow.axis = Fperp*pscale*1000000
    #print(mag(pcraft),mag(vcraft),mag(Fperp),mag(r))
    
    
    
    
    
    # Uncomment these two lines to exit the loop if
    # the spacecraft crashes onto the Earth.
    if rmag < Earth.radius: 
        break
    if mag(craft.pos-Moon.pos) < Moon.radius:
        break

    
    
    
    
    
    
    
    
    
    trail.append(pos=craft.pos)  
    t = t+deltat
print("Calculations finished after ",t, "seconds")
print("Final pos=",craft.pos," Final velo=",vcraft)