# firestore lib
from google.cloud import firestore
# Exception handler
from google.api_core.exceptions import PermissionDenied
# create_app
#import os

#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '../aerobic-factor-429519-f1-4442b62f19da.json'

def count_page_visits(request):
  try:
    db = firestore.Client()

    doc_ref = db.collection('resume-challenge').document('page-visits')
    doc = doc_ref.get()

    if doc.exists:
      data = doc.to_dict()
      current_value = data.get('visits', 0)

      new_value = current_value + 1

      doc_ref.set({ 'visits': new_value }, merge=True)

      return f"{new_value}", 200
    else:
      return "Record does not exists.", 404
  except PermissionDenied as e:
    print(e)
    return str(e), 401
  except Exception as e:
    print(e)
    return str(e), 500

#app = create_app(count_page_visits)
