//2021.08.27
//to be modified.....

const invalidJson = "{\"member\":\"미야와키 사쿠라\",\"body\":\"안녕하세요. \\(^ ^\"}";
const validJson = "{\"member\":\"미야와키 사쿠라\",\"body\":\"안녕하세요. \\\\(^ ^\"}";

type MailT = {
  member: string,
  body: string,
}

function tryCatch<T>(f: () => T): T | Error {
    try{
        return f();
    } catch (e){
        return e;
    }
}

// function(){ return JSON.parse(json) }
// () => { return JSON.parse(json) }
// () => JSON.parse(json)

const parseJson = (json: string) => tryCatch(() => JSON.parse(json))

type Try<T> = T | Error;

function mapTry<A,B>(f: (a: A) => B): (tryA: Try<A>) => Try<B> {
    return function(tryA: Try<A>){
        if (tryA instanceof Error){
            return tryA;  // Error
        }
        return f(tryA); // B
    }
}


type Either<L, R> = L | R;

function biMap<A, B, G>(
    onSuccess: (a: A) => B,
    onError: (e: Error) => G,    
): (tryA: Either<A,Error>) => Either<B,G> {
    return function(tryA: Try<A>){
        if (tryA instanceof Error){
            return onError(tryA);  // Error
        }
        return onSuccess(tryA); // B
    }
}

const onErrorHandler = (e: Error) => `<li>에러입니다!! ${e.message}</li>`;

const Mail = biMap(
    (mail: MailT) => `<li>${mail.member} : ${mail.body}</li>`,
    onErrorHandler
)

const mailValid: Try<MailT>  = parseJson(validJson);
const mailInvalid: Try<MailT> = parseJson(invalidJson);

console.log(Mail(mailValid));
console.log(Mail(mailInvalid));
