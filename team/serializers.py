from rest_framework import serializers
from .models import Member

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"
        
    def validate_name(self, value):
        if len(value) < 5:
            raise serializers.ValidationError (
                "Name must be atleast 5 characters"
            ) 
        return value    
            
    def validate_image(self,  value):
        
        max_size = 2 * 1024 * 1024
        
        if value.size > max_size:
            raise serializers.ValidationError(
                "File should be 2MB or less"
            )
        allowed_extensions = ["jpeg", "jpg", "png", "webp"]
        extension = value.name.split(".")[-1].lower()
        
        if extension not in allowed_extensions:
            raise serializers.ValidationError(
                "Only JPG, JPEG, PNG and WEBP images are allowed."
            )

        return value    
                
        
        
    
    