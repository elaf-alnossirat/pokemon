import pygame
import sys
import cv2
from models.pokemon import Pokemon

class PokemonInterface:
    def __init__(self, width=1000, height=600, video_path="assets/background/video2-background.mp4"):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Red Pokémon")

        # Load video with OpenCV
        self.video = cv2.VideoCapture(video_path)
        self.width, self.height = width, height

        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GRAY = (200, 200, 200)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)

        # Fonts
        self.title_font = pygame.font.Font(None, 50)
        self.text_font = pygame.font.Font(None, 30)

        # Load Pokéball image
        self.pokeball_image = pygame.image.load("assets/pokeball.png")
        self.pokeball_image = pygame.transform.scale(self.pokeball_image, (70, 70))

    def read_video_frame(self):
        """Reads a frame from the video and converts it for Pygame."""
        ret, frame = self.video.read()
        if not ret:  # If video ends, restart it
            self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = self.video.read()
        
        # Convert OpenCV (BGR -> RGB) and resize
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (self.width, self.height))

        # Convert image to Pygame surface
        return pygame.surfarray.make_surface(frame.swapaxes(0, 1))

    def choose_pokemon(self, available_pokemon):
        """Display the list of available Pokémon to choose from."""
        clock = pygame.time.Clock()
        buttons = [(pokemon.name, (900, 200 + (i * 100))) for i, pokemon in enumerate(available_pokemon)]

        while True:
            self.screen.fill(self.WHITE)
            background_surface = self.read_video_frame()
            self.screen.blit(background_surface, (0, 0))  # Display video background

            for text, pos in buttons:
                x, y = pos
                button_rect = pygame.Rect(x - 35, y - 35, 70, 70)
                
                # Draw Pokéball instead of rectangle
                self.screen.blit(self.pokeball_image, (button_rect.x, button_rect.y))
                
                # Render text
                text_surface = self.text_font.render(text, True, self.BLACK)
                text_rect = text_surface.get_rect(center=(x, y + 50))
                self.screen.blit(text_surface, text_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for i, (text, pos) in enumerate(buttons):
                        button_rect = pygame.Rect(pos[0] - 35, pos[1] - 35, 70, 70)
                        if button_rect.collidepoint(event.pos):
                            return available_pokemon[i]  # Return selected Pokémon

            pygame.display.flip()
            clock.tick(30)  # Adjust speed (FPS)

    def main_menu(self):
        """Display the main menu with options."""
        clock = pygame.time.Clock()
        buttons = [
            ("Start Game", (100, 50)),
            ("Add Pokémon", (350, 50)),
            ("View Pokédex", (600, 50)),
            ("Quit", (900, 50))
        ]
        
        while True:
            self.screen.fill(self.WHITE)
            background_surface = self.read_video_frame()
            self.screen.blit(background_surface, (0, 0))  # Display video background

            for text, pos in buttons:
                x, y = pos
                button_rect = pygame.Rect(x - 35, y - 35, 70, 70)
                
                # Draw Pokéball instead of rectangle
                self.screen.blit(self.pokeball_image, (button_rect.x, button_rect.y))
                
                # Render text
                text_surface = self.text_font.render(text, True, self.BLACK)
                text_rect = text_surface.get_rect(center=(x, y + 50))
                self.screen.blit(text_surface, text_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for i, (text, pos) in enumerate(buttons):
                        button_rect = pygame.Rect(pos[0] - 35, pos[1] - 35, 70, 70)
                        if button_rect.collidepoint(event.pos):
                            return i  # Return index of selected option

            pygame.display.flip()
            clock.tick(30)  # Adjust speed (FPS)

    def start(self):
        while True:
            choice = self.main_menu()
            if choice == 0:
                print("Starting game...")
            elif choice == 1:
                print("Adding a Pokémon...")
            elif choice == 2:
                print("Displaying Pokédex...")

if __name__ == "__main__":
    game = PokemonInterface()
    game.start()
