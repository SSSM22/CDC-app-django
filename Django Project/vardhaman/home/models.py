from django.db import models

# Create your models here.
class R21(models.Model):
    rank = models.IntegerField(db_column='Rank', blank=True, null=True)  # Field name made lowercase.
    roll_number = models.CharField(db_column='Roll_Number', primary_key=True, max_length=12)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=39, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=7, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=16, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    last_login = models.DateField(db_column='LAST_LOGIN', blank=True, null=True)  # Field name made lowercase.
    mobile = models.BigIntegerField(db_column='Mobile')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    hackerrank_username = models.CharField(db_column='HackerRank_UserName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    algorithms_hackerrank_field = models.CharField(db_column='Algorithms(Hackerrank)', max_length=16)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    codechef_username = models.CharField(db_column='CodeChef_UserName', max_length=19, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    cc_problems_solved = models.CharField(db_column='CC_Problems_Solved', max_length=31, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    total_ccps_10_field = models.CharField(db_column='Total(CCPS*10)', max_length=14, db_collation='utf8mb3_general_ci')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    codeforces_username = models.CharField(db_column='Codeforces_UserName', max_length=24, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    cf_problems_solved = models.CharField(db_column='CF_Problems_Solved', max_length=31, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    total_cfps_10_field = models.CharField(db_column='Total(CFPS*10)', max_length=14, db_collation='utf8mb3_general_ci')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    spoj_username = models.CharField(db_column='Spoj_UserName', max_length=19, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    spoj_problems_solved = models.CharField(db_column='Spoj_Problems_Solved', max_length=30, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    total_sps_20_field = models.CharField(db_column='Total(SPS*20)', max_length=13, db_collation='utf8mb3_general_ci')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    overall_score = models.IntegerField(db_column='Overall_Score')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'r21'