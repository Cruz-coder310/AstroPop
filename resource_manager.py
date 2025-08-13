# resource_manager.py

import pygame


class ResourceManager:
    _instance = None  # Para asegurar que solo haya una instancia (patrón Singleton)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ResourceManager, cls).__new__(cls)
        return cls._instance

    def __init__(self, options=None):
        # Evitar reinicializar si ya existe
        if hasattr(self, "initialized"):
            return

        if options is None:
            raise ValueError(
                "El ResourceManager necesita las opciones del juego para inicializarse."
            )

        print("Inicializando ResourceManager por primera vez...")
        self.options = options
        self._load_images()
        # self._load_sounds()
        self.initialized = True

    def _load_images(self):
        """Carga, escala y convierte todas las imágenes del juego."""
        print("Cargando imágenes...")
        # self.nave_img = self._prepare_image(
        #     "./images/ship.png", (self.options.ship_width,
        #                           self.options.ship_height)
        # )

        self.enemigo_img = self._prepare_image(
            "./images/enemyship.png",
            (self.options.enemy_width, self.options.enemy_height),
        )

        # self.bala_img = self._prepare_image(
        #     "./images/bullet.png",
        #     (self.options.bullet_width, self.options.bullet_height),
        # )

        # Añade aquí todas las demás imágenes que necesites
        # self.explosion_img = self._prepare_image(...)
        # self.fondo_img = pygame.image.load(...).convert()

    def _prepare_image(self, path, size):
        """Función auxiliar para preparar una imagen."""
        original_image = pygame.image.load(path)
        scale_image = pygame.transform.scale(original_image, size)
        return scale_image.convert_alpha()

    # def _load_sounds(self):
    #     """Carga todos los sonidos del juego."""
    #     print("Cargando sonidos...")
    #     # self.sonido_disparo = pygame.mixer.Sound(...)
    #     # self.sonido_explosion = pygame.mixer.Sound(...)
    #     pass  # Por ahora no hacemos nada


# Creamos una instancia global que será accesible desde cualquier parte
# Se inicializará la primera vez que se importe y se llame a su constructor
# La dejaremos como None para inicializarla desde el juego principal
resources = None


def init_manager(options):
    """Función global para inicializar el gestor de recursos."""
    global resources
    if resources is None:
        resources = ResourceManager(options)
