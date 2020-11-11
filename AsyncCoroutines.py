import asyncio
# you're actually running and keeping your shoes tied concurrently(simutaneously). You might be
# handling multiple tasks at once, but you're not really doing multiple tasks at
# once, which would be in parallel.

async def find_divisibles(inrange, div_by):
    print("finding nums in range {} divisible by {}".format(inrange, div_by))
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
        if i % 50000 == 0:
            await asyncio.sleep(0.0001)
    print("Done w/ nums in range {} divisible by {}".format(inrange, div_by))
    return located

async def main(): # make sure you wait for results before ending a script, use await
    divs1 = loop.create_task(find_divisibles(508000, 34113))
    divs2 = loop.create_task(find_divisibles(100052, 3210))
    divs3 = loop.create_task(find_divisibles(500, 3))
    await asyncio.wait([divs1,divs2,divs3])
    return divs1, divs2, divs3

if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop() # initialize loop, run the main coroutine until its done
        d1, d2, d3 = loop.run_until_complete(main())
        loop.close()
        print(d1.result())
    except Exception as e:
        print(e)
    finally:
        loop.close()

# What can we do to make it asynchronous(not happening at same time)
'''async def''' # notifies python that it is a coroutine