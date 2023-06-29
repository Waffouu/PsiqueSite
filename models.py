class Comment(models.Model):
    STATUS = (
        ('Lido', 'Lido'),
        ('Não lido', 'Não lido'),
    )



    post = models.ForeingKey(Post, on_delete=models.CASCADE)

    name = models.CharField(max_length=255, blank=False)
    comment = models.TextField()

    status = models.CharField(choices=STATUS, max_length=10, default="Não lido")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    