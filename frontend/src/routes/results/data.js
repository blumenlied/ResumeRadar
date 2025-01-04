import { userScore } from "$lib/stores/data";

let relevance_score = 0;
let exp_score = 0;
let skill_score = 0;
let pro_score = 0;

userScore.subscribe(value => {
  relevance_score = value.scores.Relevance.score;
  exp_score = value.scores.Experience.score;
  skill_score = value.scores["Skill Demonstration"].score;
  pro_score = value.scores.Professionalism.score;
})

export const data = {
  labels: ['Relevance', 'Experience', 'Skill Demonstration', 'Professionalism'],
  datasets: [
    {
      label: 'Score',
      data: [relevance_score, exp_score, skill_score, pro_score],
      fill: true,
      backgroundColor: 'rgba(255, 99, 132, 0.2)',
      borderColor: 'rgb(255, 99, 132)',
      borderWidth: 2,
      pointBackgroundColor: 'rgb(255, 99, 132)',
      pointBorderColor: '#fff',
      pointHoverBackgroundColor: '#fff',
      pointHoverBorderColor: 'rgb(255, 99, 132)',
      pointHoverRadius: 5
    }
  ]
};

