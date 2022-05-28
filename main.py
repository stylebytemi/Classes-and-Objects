class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)

    def change_name(self, name):
        self.name = name
        return self.name

    def change_age(self, age):
        self.age = age
        return self.age

    def add_track(self, tracks):
        self.tracks.append(tracks)
        return self.tracks

    def get_score(self):
        return self.score




Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
print(Bob.change_name("Peter"))
print(Bob.change_age(34))
print(Bob.add_track("UI/UX"))
print(Bob.get_score())