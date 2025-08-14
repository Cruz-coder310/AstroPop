import pygame


class ResourceManager:
    _instance = None  # Para asegurar que solo haya una instancia (patrón Singleton)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ResourceManager, cls).__new__(cls)
        return cls._instance

    def __init__(self, options):
        """initialize the attributes of the ResourceManager class."""
        self.options = options
        self._load_images()

    def _load_images(self):
        """Loads all image files from the current working directory."""
        self.nave_img = self._prepare_image(
            "./images/UFO.png", (self.options.ancho_nave, self.options.alto_nave)
        )

        self.enemigo_img = self._prepare_image(
            "./images/enemyship.png",
            (self.options.enemy_width, self.options.enemy_height),
        )

        self.bala_img = self._prepare_image(
            "./images/48.png",
            (self.options.bala_width, self.options.bala_height),
        )

    def _prepare_image(self, path, size):
        """
        returns a scaled & optimized version of the image to improve
        performance.
        """
        original_image = pygame.image.load(path)
        scale_image = pygame.transform.scale(original_image, size)
        return scale_image.convert_alpha()


# Creamos una instancia global que será accesible desde cualquier parte
# Se inicializará la primera vez que se importe y se llame a su constructor
# La dejaremos como None para inicializarla desde el juego principal
resources = None


def init_manager(options):
    """Global function to initialize the resource management system."""
    global resources
    if resources is None:
        resources = ResourceManager(options)
