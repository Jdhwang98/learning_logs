from django.db import models

# Create your models here.
class Topic(models.Model):
    # CharField is used to store small amount of text
    text = models.CharField(max_length=200)
    # DateTimeField() records date and time
    # auto_now_add=True tells Django to automatically add current date and time
    date_added = models.DateTimeField(auto_now_add=True)
    
    """ This method returns the value assigned to text attribute """
    def __str__(self): 
        return self.text
    

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "entries"
        
        def __str__(self):
            return f"{self.text[:50]}..."
    


