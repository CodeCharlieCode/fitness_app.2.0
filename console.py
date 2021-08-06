from models.exercise import Exercise
from models.user import User
from models.workout import Workout
import repositories.exercise_repository as exercise_repository 

exercise1 = Exercise("Strength","Squat", 100, 98, 1)
exercise_repository.save(exercise1)