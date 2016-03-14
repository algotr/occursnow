__author__ = 'ali'

from haystack import indexes

from .models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    created_at = indexes.DateTimeField(model_attr='created_at')
    tags = indexes.MultiValueField()
    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
