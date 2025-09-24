from django.db import models

LANGUAGE_CHOICES = [
    ('python', 'Python'),
    ('javascript', 'JavaScript'),
    ('java', 'Java'),
    ('html', 'HTML'),
]

STYLE_CHOICES = [
    ('friendly', 'Friendly'),
    ('monokai', 'Monokai'),
    ('solarized', 'Solarized'),
]

class Snippet(models.Model):
    created = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100, blank = True, default='')
    code = models.TextField()
    lineos = models.BooleanField(default=False)
    language = models.CharField(
        choices = LANGUAGE_CHOICES,
        default = 'python',
        max_length=100
    )
    style = models.CharField(
        choices=STYLE_CHOICES, 
        default='friendly', 
        max_length=100
    )
    
    class Meta:
        ordering = ['created']
        
    def __str__(self):
        return self.title or f"Snippet #{self.id}"