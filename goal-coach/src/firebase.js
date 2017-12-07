import * as firebase from 'firebase';

const config = {
    apiKey: "AIzaSyDkmDtpbMy9J8rQXubCrqvdT2MqbagcepM",
    authDomain: "goalcoach-d0918.firebaseapp.com",
    databaseURL: "https://goalcoach-d0918.firebaseio.com",
    projectId: "goalcoach-d0918",
    storageBucket: "goalcoach-d0918.appspot.com",
    messagingSenderId: "944039063769"
};

export const firebaseApp = firebase.initializeApp(config);
export const goalRef = firebase.database().ref('goals');
export const completeGoalRef = firebase.database().ref('completedGoals');