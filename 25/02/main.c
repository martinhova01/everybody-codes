#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <regex.h>
#include <sys/time.h>
#include <omp.h>

#define WALLTIME(t) ((double)(t).tv_sec + 1e-6 * (double)(t).tv_usec)

typedef struct
{
    long x;
    long y;
} ComplexNum;


ComplexNum add(ComplexNum a, ComplexNum b)
{
    ComplexNum r = {a.x + b.x, a.y + b.y};
    return r;
}

ComplexNum mul(ComplexNum a, ComplexNum b)
{
    ComplexNum r = {
        a.x * b.x - a.y * b.y,
        a.x * b.y + a.y * b.x};
    return r;
}

ComplexNum divide(ComplexNum a, ComplexNum b)
{
    ComplexNum r = {a.x / b.x, a.y / b.y};
    return r;
}

void print_complex(ComplexNum c)
{
    printf("[%ld,%ld]", c.x, c.y);
}


int extract_ints(const char *text, long *out, int max_count)
{
    regex_t regex;
    regmatch_t match;
    const char *pattern = "-?[0-9]+";

    if (regcomp(&regex, pattern, REG_EXTENDED))
    {
        fprintf(stderr, "Regex compile error\n");
        exit(1);
    }

    int count = 0;
    const char *cursor = text;

    while (count < max_count &&
           regexec(&regex, cursor, 1, &match, 0) == 0)
    {

        int start = match.rm_so;
        int end = match.rm_eo;

        char buf[64];
        int len = end - start;
        if (len >= 63)
            len = 63;

        strncpy(buf, cursor + start, len);
        buf[len] = '\0';

        out[count++] = atol(buf);

        cursor += end;
    }

    regfree(&regex);
    return count;
}


char *read_file(const char *filename)
{
    FILE *f = fopen(filename, "r");
    if (!f)
    {
        fprintf(stderr, "Cannot open file %s\n", filename);
        exit(1);
    }
    fseek(f, 0, SEEK_END);
    long size = ftell(f);
    rewind(f);

    char *buffer = malloc(size + 1);
    fread(buffer, 1, size, f);
    buffer[size] = '\0';
    fclose(f);

    return buffer;
}

int is_valid(ComplexNum num)
{
    ComplexNum res = {0, 0};
    for (int i = 0; i < 100; i++)
    {
        res = mul(res, res);
        res = divide(res, (ComplexNum){100000, 100000});
        res = add(res, num);

        if (res.x <= -1000000 || res.x >= 1000000 ||
            res.y <= -1000000 || res.y >= 1000000)
        {
            return 0;
        }
    }
    return 1;
}

ComplexNum part1(const char *filename)
{
    char *data = read_file(filename);

    long nums[2];
    extract_ints(data, nums, 2);

    ComplexNum A = {nums[0], nums[1]};
    free(data);

    ComplexNum res = {0, 0};

    for (int i = 0; i < 3; i++)
    {
        res = mul(res, res);
        res = divide(res, (ComplexNum){10, 10});
        res = add(res, A);
    }

    return res;
}

long part2(const char *filename)
{
    char *data = read_file(filename);

    long nums[2];
    extract_ints(data, nums, 2);
    free(data);

    ComplexNum A = {nums[0], nums[1]};
    ComplexNum B = add(A, (ComplexNum){1000, 1000});

    long count = 0;

#pragma omp parallel for reduction(+ : count) schedule(dynamic)
    for (long y = A.y; y <= B.y; y += 10)
    {
        for (long x = A.x; x <= B.x; x += 10)
        {
            if (is_valid((ComplexNum){x, y}))
            {
                count++;
            }
        }
    }

    return count;
}

long part3(const char *filename)
{
    char *data = read_file(filename);

    long nums[2];
    extract_ints(data, nums, 2);
    free(data);

    ComplexNum A = {nums[0], nums[1]};
    ComplexNum B = add(A, (ComplexNum){1000, 1000});

    long count = 0;

#pragma omp parallel for reduction(+ : count) schedule(dynamic)
    for (long y = A.y; y <= B.y; y++)
    {
        for (long x = A.x; x <= B.x; x++)
        {
            if (is_valid((ComplexNum){x, y}))
            {
                count++;
            }
        }
    }

    return count;
}

int main()
{
    struct timeval t_start, t_end;
    gettimeofday(&t_start, NULL);

    printf("---TEST---\n");
    ComplexNum r1 = part1("testinput1.txt");
    printf("part 1: ");
    print_complex(r1);
    printf("\n");
    printf("part 2: %ld\n", part2("testinput2.txt"));
    printf("part 3: %ld\n\n", part3("testinput3.txt"));

    printf("---MAIN---\n");
    r1 = part1("input1.txt");
    printf("part 1: ");
    print_complex(r1);
    printf("\n");
    printf("part 2: %ld\n", part2("input2.txt"));
    printf("part 3: %ld\n\n", part3("input3.txt"));

    gettimeofday(&t_end, NULL);

    printf("Total elapsed time: %lf seconds\n",
           WALLTIME(t_end) - WALLTIME(t_start));

    return 0;
}
