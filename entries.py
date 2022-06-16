from basic import db, Puppy, Owner, Toy


rufus = Puppy('Rufus', 2)
fido = Puppy('Fido', 1)

# add puppies to db
db.session.add_all([rufus, fido])
db.session.commit()


# check!
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)


# create owner
andrew = Owner('Andrew', rufus.id)

# Give Rufus a toy
toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy('Ball', rufus.id)

db.session.add_all([andrew, toy1, toy2])
db.session.commit()

# grab rufus after those additions
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)
rufus.report_toys()