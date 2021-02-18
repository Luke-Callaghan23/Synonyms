class VocabCompleter {
    constructor (vocab, delims='') {
        this.vocab         = vocab;    // List of all possible terms that the complete function could return
        this.internalState = -1;       // Internal offset into the possible completion retults of a term
        this.original      = '';       // Most recent original string that the user has typed
        this.lastResponse  = '';       // Most term that was returned by this.completion -- the string that resulted 
                                       //        from the most recent tab press
        this.delims        = delims;   // String of all possible delimiters
    }

    // This is the completion function that will be called once for every
    //       item in the this.vocab list with:
    // text  = user input from most recent whitespace character to the most 
    //       recent typed character
    // Ex -- 
    //       user string: 'ca'
    //       this.vocab: [ 'cat', 'car', 'catastrophe', 'dog', 'goose', 'california' ]
    //           When user hits tab once: 'cat',
    //           again: 'car',
    //           again: 'catastrophe',
    //           again: 'california',
    //           If the user hits tab again, we've exhausted all options, so original string is returned: 'ca',
    //           If tab is hit again, we cycle back to the beginning: 'cat',
    //           etc., etc.
    complete (input) {
        let [before, text] = this.splitOnLatestDelims(input)
        
        console.log(before, text)

        if (text != this.lastResponse) {
            // if (the 'text' parameter is different from the last response) {
            //       returned by this function, we know that the user has
            //       typed something new.
            // So, we set this.original to the user's new text
            this.original = text;
            // This also means that the below 'results' array will be 
            //       altered, so we need to also revert this.internal_state
            //       to its original value
            this.internalState = -1;
        }
        
        // this.internal_state is the internal offset into the results array
        //       so whenever tab is hit, the internal offset is incremented,
        //       and a new result in the below results array will be returned
        this.internalState += 1
        console.log(this.internalState)

        // Returns all completions strings in the this.vocab
        //       list that startswith the user's original string
        let mapped = this.vocab.map (
            x => x.toLowerCase()
        );
        let results = mapped.filter (
            x => x.toLowerCase().startsWith(this.original.toLowerCase())
        );

        if (this.original != '') {
            // If the user's text is not an empty string, then the last optio
            //       for them will be their original string
            results.push( this.original )
        }

        // The response of this function call is found by indexing into the 
        //       above results array by the current internal state offset (mapped
        //       onto the length of the results array)
        this.lastResponse = results [ this.internalState % results.length ];

        // Return the rsult
        return before + this.lastResponse;
    }

    // Function to split a string, called 'text' by the latest occurrence of any 
    //       of the chracters in this object's this.delims string, and return
    //       a tuple of all characters before and including the delim, and all
    //       characters coming before the custom delim
    splitOnLatestDelims (text) {
        for (let index = text.length - 1; index >= 0; index--) {
            const char = text[ index ]
            if (this.delims.indexOf(char) > -1) {
                let before = text.substring(0, index); 
                let after  = text.substring(index+1);
                before += char;
                return [before, after];
            }
        }
        return ['', text];
    }
}