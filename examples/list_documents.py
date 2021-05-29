"""List current photoshop all documents."""

# Import local modules
import photoshop.api as ps


app = ps.Application()

doc = app.documents[0]
print(doc.name)

for doc in app.documents:
    print(doc.name)
