import pygame


class ResourceManager:
    _instance = (
        None  # Para asegurar que solo haya una instancia (patrón Singleton)
    )

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ResourceManager, cls).__new__(cls)
        return cls._instance

    def __init__(self, game):
        """initialize the attributes of the ResourceManager class."""
        self.options = game.options
        self.rect_pnt = game.rect_pnt
        self._load_images()

    def _load_images(self):
        """Loads all image files from the current working directory."""
        self.nave_image = self._prepare_image(
            "./images/UFO.png",
            (self.options.ancho_nave, self.options.alto_nave),
        )
        self.nave_mask = pygame.mask.from_surface(self.nave_image)

        self.enemigo_image = self._prepare_image(
            "./images/enemyship.png",
            (self.options.enemy_width, self.options.enemy_height),
        )
        self.enemigo_mask = pygame.mask.from_surface(self.enemigo_image)

        self.bala_image = self._prepare_image(
            "./images/48.png",
            (self.options.bala_width, self.options.bala_height),
        )
        self.bala_mask = pygame.mask.from_surface(self.bala_image)

        self.boton_inicio = self._prepare_image("./images/boton.png")

        self.score = self._prepare_image(
            "./images/YourScoreIs.png",
            (self.rect_pnt.width * 0.6, self.rect_pnt.height * 0.1),
        )

        self.record = self._prepare_image(
            "./images/HighScores.png",
            (self.rect_pnt.width * 0.5, self.rect_pnt.height * 0.1),
        )

        self.background = self._prepare_image(
            "./images/planeta.png", self.rect_pnt.size
        )

        self.panel_pause_blue = self._prepare_image(
            "./images/panel-1.png",
            (self.rect_pnt.width * 0.6, self.rect_pnt.height * 0.5),
        )

        self.panel_pause_red = self._prepare_image(
            "./images/panel-2.png",
            (self.rect_pnt.width * 0.4, self.rect_pnt.height * 0.9),
        )

    def _prepare_image(self, path, size=None):
        """
        Loads an image from the given path & returns an optimized version.
        If size is provided, the image is scaled to that size.
        """
        try:
            original_image = pygame.image.load(path)
            if size:
                scale_image = pygame.transform.scale(original_image, size)
                return scale_image.convert_alpha()
            else:
                return original_image.convert_alpha()
        except pygame.error as e:
            print(f"Error loading image at {path}: {e}")


# Creamos una instancia global que será accesible desde cualquier parte
# Se inicializará la primera vez que se importe y se llame a su constructor
# La dejaremos como None para inicializarla desde el juego principal
resources = None


def init_manager(options):
    """Global function to initialize the resource management system."""
    global resources
    if resources is None:
        resources = ResourceManager(options)
