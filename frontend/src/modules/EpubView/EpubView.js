import React, { Component } from 'react'
import PropTypes from 'prop-types'
import Epub from 'epubjs/lib/index'
import defaultStyles from './style'

class EpubView extends Component {
  constructor(props) {
    super(props)
    this.state = {
      isLoaded: false,
      toc: []
    }
    this.viewerRef = React.createRef()
    this.location = props.location
    this.book = this.rendition = this.prevPage = this.nextPage = null
    this.initBook(true)
  }

  initBook() {
    const { url, tocChanged, epubInitOptions } = this.props
    this.book = new Epub(url, epubInitOptions)
    this.book.loaded.navigation.then(({ toc }) => {
      this.setState(
        {
          isLoaded: true,
          toc: toc
        },
        () => {
          tocChanged && tocChanged(toc)
          this.initReader()
        }
      )
    })
  }

  initReader() {
    const { toc } = this.state
    const { location, epubOptions, getRendition } = this.props
    const node = this.viewerRef.current
    this.rendition = this.book.renderTo(node, {
      contained: true,
      width: '100%',
      height: '100%',
      ...epubOptions
    })

    this.prevPage = () => {
      this.rendition.prev()
    }
    this.nextPage = () => {
      this.rendition.next()
    }
    this.registerEvents()
    getRendition && getRendition(this.rendition)

    if (typeof location === 'string' || typeof location === 'number') {
      this.rendition.display(location)
    } else if (toc.length > 0 && toc[0].href) {
      this.rendition.display(toc[0].href)
    } else {
      this.rendition.display()
    }
  }

  registerEvents() {
    const { handleKeyPress, handleTextSelected } = this.props
    this.rendition.on('locationChanged', this.onLocationChange)
    this.rendition.on('keyup', handleKeyPress || this.handleKeyPress)
    if (handleTextSelected) {
      this.rendition.on('selected', handleTextSelected)
    }
  }

  onLocationChange = loc => {
    const { location, locationChanged } = this.props
    const newLocation = loc && loc.start
    if (location !== newLocation) {
      this.location = newLocation
      locationChanged && locationChanged(newLocation)
    }
  }

  renderBook() {
    const { styles } = this.props
    return <div ref={this.viewerRef} style={styles.view} />
  }

  handleKeyPress = ({ key }) => {
    key && key === 'ArrowRight' && this.nextPage()
    key && key === 'ArrowLeft' && this.prevPage()
  }
/**
<script src=location></script>
<script>
var ExcelToJSON = function() {
  this.parseExcel = function(file) {
    var reader = new FileReader();
    reader.onload = function(e) {
      var data = e.target.result;
      var workbook = XLSX.read(data, {
        type: 'binary'
      });
      workbook.SheetNames.forEach(function(sheetName) {
        var XL_row_object = XLSX.utils.sheet_to_row_object_array(workbook.Sheets[sheetName]);
      })
    };
    };
  };
};
</script>
**/

/**
function search( obj, value, path ) {
  var keys = Object.keys(obj);
  for( var i=0; i<keys.length; i++ ) {
    if(obj[ keys[i] ] === value) {
       return keys[i+1];
    }
  }
  return "word not found";
}
**/
  render() {
    const { isLoaded } = this.state
    const { loadingView, styles } = this.props
    return (
      <div style={styles.viewHolder}>
        {(isLoaded && this.renderBook()) || loadingView}
        //call the excel to JSON function and input the source file in that function above
        //call search on the word value with the new excel variable that was created in excel function
        //super simple search functionality that needs testing
      </div>
    )
  }
}

EpubView.defaultProps = {
  loadingView: null,
  locationChanged: null,
  tocChanged: null,
  styles: defaultStyles,
  epubOptions: {},
  epubInitOptions: {}
}

EpubView.propTypes = {
  url: PropTypes.oneOfType([
    PropTypes.string,
    PropTypes.instanceOf(ArrayBuffer)
  ]),
  loadingView: PropTypes.element,
  location: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
  locationChanged: PropTypes.func,
  tocChanged: PropTypes.func,
  styles: PropTypes.object,
  epubInitOptions: PropTypes.object,
  epubOptions: PropTypes.object,
  getRendition: PropTypes.func,
  handleKeyPress: PropTypes.func,
  handleTextSelected: PropTypes.func
}

export default EpubView
