/**
 * Algebra 2 Unit 4 Lesson 1 Quiz — Google Forms Auto-Creator
 *
 * HOW TO USE:
 * 1. Go to https://script.google.com
 * 2. Create a new project
 * 3. Paste this entire script
 * 4. Click Run > createQuiz
 * 5. Authorize when prompted
 * 6. Check your Google Drive for "Algebra 2 Unit 4 Lesson 1 Quiz"
 */

function createQuiz() {
  var form = FormApp.create('Algebra 2 Unit 4 Lesson 1 Quiz');
  form.setDescription(
    'Inverse Variation and the Reciprocal Function.\n' +
    'This quiz covers only Lesson 1 content aligned to the Topic 4 assessment.\n' +
    'Assessment anchors: TTB1, TTB5, TTB14 (core) + TTB16 (extension).'
  );
  form.setIsQuiz(true);
  form.setShuffleQuestions(false);

  // ── Q1: Fill-in (inverse variation table) ──
  var q1 = form.addTextItem();
  q1.setTitle(
    'The chart represents an inverse variation. Find the value of p.\n\n' +
    'x:  3,   10,  15,  30\n' +
    'y:  5,    p,    1,  0.5'
  );
  q1.setRequired(true);
  q1.setPoints(1);
  var q1Validation = FormApp.createTextValidation()
    .setHelpText('Enter a number.')
    .requireNumber()
    .build();
  q1.setValidation(q1Validation);
  // Note: Text items can't auto-grade in Forms. Add answer key manually: 1.5

  // ── Q2: Multiple choice (equation from table) ──
  var q2 = form.addMultipleChoiceItem();
  q2.setTitle(
    'Write an equation for the inverse variation represented by the table.\n\n' +
    'x:  -3,   -1,   1/2,   2/3\n' +
    'y:   4,    12,  -24,   -18'
  );
  q2.setRequired(true);
  q2.setPoints(1);
  q2.setChoices([
    q2.createChoice('y = x/(-12)', false),
    q2.createChoice('y = 12/x', false),
    q2.createChoice('y = -x/12', false),
    q2.createChoice('y = -12/x', true)
  ]);
  q2.setFeedbackForCorrect(
    FormApp.createFeedback()
      .setText('Correct! k = (-3)(4) = -12, so y = -12/x.')
      .build()
  );
  q2.setFeedbackForIncorrect(
    FormApp.createFeedback()
      .setText('Incorrect. Find k by multiplying any x-y pair: (-3)(4) = -12. The equation is y = -12/x.')
      .build()
  );

  // ── Q3: Multiple choice (application) ──
  var q3 = form.addMultipleChoiceItem();
  q3.setTitle(
    'Three students can wash a car in 16 minutes. If the time varies inversely ' +
    'with the number of students washing the car, how many minutes will it take ' +
    'two students to complete that same job?'
  );
  q3.setRequired(true);
  q3.setPoints(1);
  q3.setChoices([
    q3.createChoice('20', false),
    q3.createChoice('22', false),
    q3.createChoice('24', true),
    q3.createChoice('26', false)
  ]);
  q3.setFeedbackForCorrect(
    FormApp.createFeedback()
      .setText('Correct! k = 3 * 16 = 48. Time = 48 / 2 = 24 minutes.')
      .build()
  );
  q3.setFeedbackForIncorrect(
    FormApp.createFeedback()
      .setText('Incorrect. Since time varies inversely with students: k = 3 * 16 = 48. For 2 students: 48 / 2 = 24.')
      .build()
  );

  // ── Q4: Fill-in (horizontal asymptote) ──
  var q4 = form.addTextItem();
  q4.setTitle(
    'What is the equation of the horizontal asymptote of the graph of\n' +
    'y = 1/(x + 5) - 4 ?\n\n' +
    'Write your answer in the form y = ___'
  );
  q4.setRequired(true);
  q4.setPoints(1);
  // Note: Text items can't auto-grade. Add answer key manually: y = -4

  // ── Q5: Multiple choice (translation) ──
  var q5 = form.addMultipleChoiceItem();
  q5.setTitle(
    'The graph of y = 1/x is translated 3 units up and 2 units to the left. ' +
    'What is an equation of the translated graph?'
  );
  q5.setRequired(true);
  q5.setPoints(1);
  q5.setChoices([
    q5.createChoice('y = 1/(x + 2) + 3', true),
    q5.createChoice('y = 1/(x - 2) + 3', false),
    q5.createChoice('y = 1/(x - 3) + 2', false),
    q5.createChoice('y = 1/(x + 3) - 2', false)
  ]);
  q5.setFeedbackForCorrect(
    FormApp.createFeedback()
      .setText('Correct! Left 2 means (x + 2) in the denominator, and up 3 means + 3 outside.')
      .build()
  );
  q5.setFeedbackForIncorrect(
    FormApp.createFeedback()
      .setText('Incorrect. For y = 1/(x - h) + k: left 2 means h = -2, so (x + 2). Up 3 means k = 3. Answer: y = 1/(x + 2) + 3.')
      .build()
  );

  Logger.log('Quiz created: ' + form.getEditUrl());
  Logger.log('Student link: ' + form.getPublishedUrl());
}
