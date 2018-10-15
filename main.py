from direct.showbase.ShowBase import ShowBase
import panda3d.core


class App(ShowBase):
    def __init__(self):
        super().__init__()
        self.model = base.loader.loadModel('env.bam')
        self.model.reparentTo(base.render)

        # Fix the camera angle
        base.camera.setPosHpr(self.model.find('Camera'), 0, 0, 0, 0, -90, 0)
        base.disableMouse()

        cm = panda3d.core.CardMaker('TestCard')

        for i in range(20):
            cardFrame = base.render.attachNewNode(cm.generate())
            # Transparency must be enabled for bug to happen.
            cardFrame.setTransparency(True)


app = App()
app.run()
