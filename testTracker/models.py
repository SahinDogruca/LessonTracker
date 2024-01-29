from django.db import models
from questionTracker.models import Area, Class, Lesson


class AreaTest(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="Alan")
    name = models.CharField(max_length=255, verbose_name="İsim", blank=True, null=True)
    date = models.DateTimeField(verbose_name="Tarih")
    visible = models.BooleanField(verbose_name="Görünürlük",blank=True,null=True)
    
    def __str__(self):
        return (
            self.name
            if self.name != None and self.name != ""
            else f"{self.area} Test {self.id}"
        )

    def get_total_score(self):
        branch_test = BranchTest.objects.filter(area_test=self.id)
        score = 100

        for b_test in branch_test:
            score += b_test.get_score()
        return round(score, 3)

    def get_title(self):
        return (
            self.name
            if self.name != None and self.name != ""
            else f"{self.area} Test {self.id}"
        )

    def get_date(self):
        return self.date.strftime("%d %B %Y, %A")
    
    
    def get_social(self):
        branch_test = BranchTest.objects.filter(area_test=self.id)

        question_total = 0
        true_question = 0
        false_question = 0
        blank_question = 0
        clear_question = 0
        for b_test in branch_test:
            if b_test.lesson.name in ["Tarih", "Coğrafya", "Felsefe", "Din"]:
                true_question += b_test.true_question
                false_question += b_test.false_question
                blank_question += b_test.get_blank_question()
                clear_question += b_test.get_clear_question()

        return f"Sosyal {true_question} | {false_question} | {blank_question} | {clear_question}\n"
    
    
    def get_science(self):
        branch_test = BranchTest.objects.filter(area_test=self.id)

        question_total = 0
        true_question = 0
        false_question = 0
        blank_question = 0
        clear_question = 0
        for b_test in branch_test:
            if b_test.lesson.name in ["Fizik", "Kimya", "Biyoloji"]:
                true_question += b_test.true_question
                false_question += b_test.false_question
                blank_question += b_test.get_blank_question()
                clear_question += b_test.get_clear_question()

        return f"Fen      {true_question} | {false_question} | {blank_question} | {clear_question} \n"

    def get_total_infos(self):
        branch_test = BranchTest.objects.filter(area_test=self.id)

        question_total = 0
        true_question = 0
        false_question = 0
        blank_question = 0
        clear_question = 0
        for b_test in branch_test:
            true_question += b_test.true_question
            false_question += b_test.false_question
            blank_question += b_test.get_blank_question()
            clear_question += b_test.get_clear_question()

        return [true_question, false_question, blank_question, clear_question]


class BranchTest(models.Model):
    area = models.ForeignKey(
        Area, on_delete=models.CASCADE, verbose_name="Alan", blank=True, null=True
    )
    clas = models.ForeignKey(
        Class, on_delete=models.CASCADE, verbose_name="Sınıf", blank=True, null=True
    )
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Ders")
    name = models.CharField(max_length=255, verbose_name="İsim", blank=True, null=True)
    total_question = models.PositiveIntegerField(verbose_name="Soru Sayısı")
    true_question = models.PositiveIntegerField(verbose_name="Doğru Soru Sayısı")
    false_question = models.PositiveIntegerField(verbose_name="Yanlış Soru Sayısı")
    date = models.DateTimeField(auto_now=True, verbose_name="Tarih")
    area_test = models.ForeignKey(
        AreaTest, on_delete=models.CASCADE, blank=True, null=True
    )

    def get_score(self):
        if self.area_test.area.name == "Tyt":
            if self.lesson.name == "Matematik" or self.lesson.name == "Edebiyat":
                k = 3.3
            else:
                k = 3.4
        else:
            if self.lesson.name == "Matematik":
                k = 3
            elif self.lesson.name == "Fizik":
                k = 2.85
            else:
                k = 3.07
        return self.get_clear_question() * k

    def get_blank_question(self):
        return self.total_question - (self.true_question + self.false_question)

    def get_clear_question(self):
        penalty_question = round(self.false_question / 4, 2)
        return self.true_question - (penalty_question)

    def __str__(self):
        return (
            self.name
            if self.name != None and self.name != ""
            else f"{self.lesson} Test {self.id}"
        )

    def get_title(self):
        return (
            self.name
            if self.name != None and self.name != ""
            else f"{self.lesson} Test {self.id}"
        )

    def get_date(self):
        return self.date.strftime("%d %A %Y")
