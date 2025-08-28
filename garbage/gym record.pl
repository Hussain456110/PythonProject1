% User Profile: user(Name, Age, FitnessLevel, Goal, HealthConditions).
user(john, 30, intermediate, weight_loss, [none]).
user(mary, 50, beginner, flexibility, [joint_pain]).
user(alex, 25, advanced, muscle_gain, [none]).
user(susan, 35, beginner, endurance, [asthma]).

% Exercise: exercise(Name, Type, Difficulty, SuitableForGoals, Restrictions).
exercise(jogging, cardio, beginner, [weight_loss, endurance], [asthma]).
exercise(yoga, flexibility, beginner, [flexibility, relaxation], [joint_pain]).
exercise(weightlifting, strength, advanced, [muscle_gain], [joint_pain]).
exercise(swimming, cardio, intermediate, [weight_loss, endurance], [none]).
exercise(pilates, flexibility, intermediate, [flexibility, relaxation], [none]).
exercise(pushups, strength, beginner, [muscle_gain], [none]).
exercise(cycling, cardio, intermediate, [endurance, weight_loss], [asthma]).
exercise(plank, strength, intermediate, [muscle_gain, endurance], [none]).
exercise(deep_breathing, relaxation, beginner, [relaxation, endurance], [none]).
exercise(burpees, cardio, advanced, [weight_loss, endurance], [none]).
exercise(dumbbell_curls, strength, beginner, [muscle_gain], [none]).

% Hydration reminders
hydration_reminder(User, Reminder) :-
    user(User, _, _, _, _),
    Reminder = "Remember to drink water every 30 minutes during your workout to stay hydrated.".

% Suggest active recovery days
active_recovery_day(User, RecoveryActivity) :-
    user(User, _, FitnessLevel, _, HealthConditions),
    (FitnessLevel = beginner, RecoveryActivity = "Light yoga or walking";
     FitnessLevel = intermediate, RecoveryActivity = "Swimming or pilates";
     FitnessLevel = advanced, RecoveryActivity = "Dynamic stretches or foam rolling"),
    \+ (member(joint_pain, HealthConditions), RecoveryActivity = "High-impact activities").

% Recommend music playlists for workouts
workout_music(User, Playlist) :-
    user(User, _, FitnessLevel, Goal, _),
    (Goal = weight_loss, Playlist = "High-energy beats";
     Goal = muscle_gain, Playlist = "Heavy lifting rock";
     Goal = flexibility, Playlist = "Calm and relaxing tunes";
     Goal = endurance, Playlist = "Long-run motivating tracks"),
    (FitnessLevel = beginner, Playlist = Playlist;
     FitnessLevel = intermediate, atom_concat(Playlist, " - Intermediate Edition", Playlist);
     FitnessLevel = advanced, atom_concat(Playlist, " - Advanced Edition", Playlist)).

% Provide workout schedule
workout_schedule(User, Schedule) :-
    user(User, _, FitnessLevel, _, _),
    (FitnessLevel = beginner, Schedule = ["Monday: Light Cardio", "Wednesday: Yoga", "Friday: Strength Training"];
     FitnessLevel = intermediate, Schedule = ["Tuesday: Jogging", "Thursday: Pilates", "Saturday: Swimming"];
     FitnessLevel = advanced, Schedule = ["Monday: Weightlifting", "Wednesday: Cycling", "Friday: HIIT"]).

% Calculate BMI
calculate_bmi(User, Height, Weight, BMI, Category) :-
    user(User, _, _, _, _),
    BMI is Weight / (Height * Height),
    (BMI < 18.5, Category = underweight;
     BMI >= 18.5, BMI < 24.9, Category = normal;
     BMI >= 25, BMI < 29.9, Category = overweight;
     BMI >= 30, Category = obese).

% Suggest fitness gadgets
fitness_gadgets(User, Gadgets) :-
    user(User, _, FitnessLevel, _, _),
    (FitnessLevel = beginner, Gadgets = [step_counter, yoga_mat];
     FitnessLevel = intermediate, Gadgets = [fitness_band, foam_roller];
     FitnessLevel = advanced, Gadgets = [smartwatch, resistance_bands, weightlifting gloves]).

% Goal completion tracker
goal_progress(User, TotalGoals, CompletedGoals, Progress) :-
    user(User, _, _, _, _),
    Progress is (CompletedGoals / TotalGoals) * 100.

% Mood-based exercise suggestions
exercise_for_mood(Mood, Exercise) :-
    (Mood = energetic, Exercise = "High-intensity interval training (HIIT)";
     Mood = relaxed, Exercise = "Yoga or deep breathing";
     Mood = stressed, Exercise = "Pilates or walking";
     Mood = focused, Exercise = "Weightlifting or cycling").

% Partner compatibility for group workouts
partner_compatibility(User, Partner, Compatibility) :-
    user(User, _, FitnessLevel, Goal, _),
    user(Partner, _, FitnessLevel, Goal, _),
    User \= Partner,
    Compatibility = "Good match for group workouts".

% Reward system for consistency
reward_system(User, DaysCompleted, Reward) :-
    user(User, _, _, _, _),
    (DaysCompleted >= 7, Reward = "Bronze badge for consistency!";
     DaysCompleted >= 14, Reward = "Silver badge for persistence!";
     DaysCompleted >= 30, Reward = "Gold badge for dedication!").

% Query examples:
% ?- hydration_reminder(john, Reminder).
% ?- active_recovery_day(mary, RecoveryActivity).
% ?- workout_music(alex, Playlist).
% ?- workout_schedule(susan, Schedule).
% ?- calculate_bmi(john, 1.75, 70, BMI, Category).
% ?- fitness_gadgets(john, Gadgets).
% ?- goal_progress(mary, 10, 5, Progress).
% ?- exercise_for_mood(energetic, Exercise).
% ?- partner_compatibility(john, alex, Compatibility).
% ?- reward_system(alex, 15, Reward).
