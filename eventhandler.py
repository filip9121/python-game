#Main has event handler
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True
