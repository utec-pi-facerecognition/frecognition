def backend_face_comparation(_embeddings_to_compare, _dataset_of_embeddings):
  identified_faces = []
  
  def inline_knn(dot, l_dots, l_name, d_name, k):
    return [ l_dis['l'] for l_dis in sorted([{'l' : l_dot[l_name], 'd' : (sum([(x-y)**(2) for x, y in zip(dot, l_dot[d_name])]))**(1/2)} for l_dot in l_dots], key=lambda x: x['d'])[0:k] ]
  
  for _embedding in _embeddings_to_compare:
    # IMPORTANTE
    # Cambiar 'codigo' y 'atributos' por las etiquetas correspondientes del dataset
    identified_faces.append(inline_knn(_embedding, _dataset_of_embeddings, 'codigo', 'atributos', 1)[0])
  
  return identified_faces
