from django.shortcuts import _get_queryset

def get_object_or_None(klass, *args, **kwargs):
    """
      Esta funcion maneja excepciones como get_object_or_404
    """
    queryset = _get_queryset(klass)
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        return None
