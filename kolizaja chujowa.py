for sprite in self.stop.sprites():
    if (self.direction == 0 or self.direction == 1) and sprite.rect.colliderect(self.rect):
        if self.direction == 0:
            self.x_pos -= self.speed
        elif self.direction == 1:
            self.x_pos += self.speed
        self.direction = randint(2, 3)
        self.turns[self.direction] = True

    elif (self.direction == 2 or self.direction == 3) and sprite.rect.colliderect(self.rect):
        if self.direction == 2:
            self.y_pos += self.speed
        elif self.direction == 3:
            self.y_pos -= self.speed
        self.direction = randint(0, 1)
        self.turns[self.direction] = True
counter = 0
for t in self.turns:
    if t == False:
        counter += 1
if counter == 4:
    self.turns[self.direction] = True
if self.direction == 0:
    self.x_pos += self.speed
elif self.direction == 1:
    self.x_pos -= self.speed
elif self.direction == 2:
    self.y_pos -= self.speed
elif self.direction == 3:
    self.y_pos += self.speed
print(self.direction)