from tortoise import Model, fields


class Ores(Model):
    id = fields.IntField(pk=True)
    stone = fields.IntField(default=0)
    iron = fields.IntField(default=0)
    gold = fields.IntField(default=0)
    diamond = fields.IntField(default=0)
    void = fields.IntField(default=0)

    @property
    def raw_counts(self):
        return {
            'stone': self.stone,
            'iron': self.iron,
            'gold': self.gold,
            'diamond': self.diamond,
            'void': self.void,
        }