from rest_framework import serializers;
from books_api.models import Book;

# This is means DTO, response type object like that
# Convert complex data sturctures into python data structures
class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True);
    title = serializers.CharField();  
    number_of_pages = serializers.IntegerField();
    publish_date = serializers.DateField();
    quantity = serializers.IntegerField();

    def create(self, data):
        return Book.objects.create(**data);

    def update(self, instance, data):
        instance.title = data.get('title', instance.title);
        instance.number_of_pages = data.get('number_of_pages', instance.number_of_pages);
        instance.publish_date = data.get('publish_date', instance.publish_date);
        instance.quantity = data.get('quantity', instance.quantity);

        instance.save();
        return instance;